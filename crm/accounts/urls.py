from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='product'),
    path('customers/<str:pk>/',views.customers,name='customer'),
    path('create-order/<str:pk>',views.createOrder,name='create-order'),
    path('update-order/<str:pk>/',views.updateOrder,name='update-order'),
    path('delete-order/<str:pk>/',views.deleteOrder,name='delete-order'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('user/',views.userPage,name='user-page'),
    path('account/',views.accountsettings,name='account'),
    path('reset_password/',auth_views.PasswordResetView.as_view(
        template_name='accounts/PassWordReset.html'
    ),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/PassWordResetSent.html'
    ),name='password_reset_done'),
    path('reset/<uidb64>>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/PassWordResetForm.html'
    ),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/PassWordResetdone.html'
    ),name='password_reset_complete'),
]





