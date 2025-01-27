from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('signup', views.SignupPage, name = 'signup'),
    path('login', views.UserLoginView.as_view(), name = 'login'),
    path('changepasswithprev/', views.ChangePasswordView.as_view(), name='changepasswithprev'),
    path('logout/', views.LogoutPage, name='logout'),
    path('profile/', views.ProfilePage, name='profile'),
    path('brandpage/<int:id>', views.BrandPage, name='brandpage'),
    path('carpage/<int:id>', views.CarPage, name='carpage'),
    path('updateprofile/', views.ProfileUpdateView.as_view(), name='profileupdate'),
    path('checkout/<int:id>', views.Checkout, name='checkout'),
    path('ordersprofile/', views.OrdersProfilePage, name='ordersprofile'),
    
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)