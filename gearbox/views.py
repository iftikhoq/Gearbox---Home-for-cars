from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SignupForm, LoginForm, UpdateProfileForm, ReplyForm, CommentForm
from django.contrib import messages 
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm 
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from cars import models as cmodels
from customuser import models as cusmodels
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

def Home(request):
    cars = cmodels.Cars.objects.all()
    brands = cmodels.Brand.objects.all()
    return render(request, 'index.html', {'brands': brands, 'cars': cars, 'carscount': cars.count})

def BrandPage(request, id):
    brands = cmodels.Brand.objects.all()
    brand = get_object_or_404(cmodels.Brand, pk=id)
    cars = cmodels.Cars.objects.filter(brand=brand)
    return render(request, 'index.html', {'cars': cars, 'brands': brands, 'carscount': cars.count})

def CarPage(request, id):
    car = get_object_or_404(cmodels.Cars, pk=id)
    comments = car.comments.all()

    if request.method == "POST":
        if "comment_submit" in request.POST:
            commentform = CommentForm(request.POST)
            if commentform.is_valid():
                comment = commentform.save(commit=False)
                comment.car = car
                comment.user = request.user
                comment.save()
                return redirect("carpage", id=car.id)
        elif "reply_submit" in request.POST:
            replyform = ReplyForm(request.POST)
            if replyform.is_valid():
                reply = replyform.save(commit=False)
                reply.user = request.user
                reply.comment = cmodels.Comment.objects.get(id=request.POST.get("cid"))
                reply.save()
                return redirect("carpage", id=car.id)

    commentform = CommentForm()
    replyform = ReplyForm()

    return render(
        request,
        "carpage.html",
        {"car": car, "comments": comments, "commentform": commentform, "replyform": replyform},
    )

@login_required
def Checkout(request,id):
    if request.method == 'POST':
        carid = request.POST.get('carid')
        address = request.POST.get('address')
        trxid = request.POST.get('trxid')
        total = request.POST.get('total')

        car = get_object_or_404(cmodels.Cars, pk=carid)
        car.quantity = car.quantity - 1
        car.save()
        order = cusmodels.Orders(address = address, TRXid=trxid, car = car, customer = request.user, totalamount=total)
        order.save()
        return redirect('profile')  
    else:
        car = get_object_or_404(cmodels.Cars, pk=id)
        return render(request, 'checkout.html', {'car': car})

@login_required
def OrdersProfilePage(request):
    orders = cusmodels.Orders.objects.filter(customer = request.user)
    brands = cmodels.Brand.objects.all()
    return render(request, 'cusorders.html', {'orders': orders})


def SignupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Signup successful! Welcome, {user.username}.')
            return redirect('login')
        else:
            messages.error(request, 'Signup failed. Please correct the errors below.')
    else: 
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form}) 


def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('profile')  
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please fill out form correctly.")
    else:
        form = LoginForm()  
    
    return render(request, 'login.html', {'form': form})


def LogoutPage(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

@login_required
def ProfilePage(request):
    return render(request, 'profile.html')

def Changepasswithprev(request):
    if request.method  ==  'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "You have successfully changed password.")
            return redirect('profile')
        else:
            messages.error(request, "Please fill out form correctly.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepasswithprev.html', {'form': form}) 


class UserLoginView(LoginView):
    template_name = 'login.html' 
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']= 'Login'
        return context

    def get_success_url(self):
        return self.success_url

@login_required
def ProfileUpdate(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'profileupdate.html', {'form': form})