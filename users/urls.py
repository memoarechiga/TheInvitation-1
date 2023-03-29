from django.urls import path
from .views import MyLoginView, RegisterView, ProfileList, ProfileDetail, ProfileUpdate #, profile



from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('login/', MyLoginView.as_view(redirect_authenticated_user=True),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('password-reset/', 
        PasswordResetView.as_view(
            template_name='users/password_reset.html',
            html_email_template_name='users/password_reset_email.html'
        ),
        name='password-reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
        
    path('profilelist/', ProfileList.as_view(), name='profilelist'),
    path('profiledetail/<int:pk>/',ProfileDetail.as_view(),name='profiledetail'),
    path('profileupdate/<int:pk>/',ProfileUpdate.as_view(), name='profileupdate'),

]



