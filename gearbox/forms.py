from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from customuser.models import CustomUser
from cars.models import Comment, Reply

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name' , 'last_name', 'email', 'phone', 'address']

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            'content': forms.Textarea(attrs={'cols': 40, 'rows': 1})  
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["content"]
        widgets = {
            'content': forms.Textarea(attrs={'cols': 40, 'rows': 1})  
        }
