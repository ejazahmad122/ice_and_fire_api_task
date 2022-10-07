from django.urls import path
from .views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserRegistrationView, UserResetPasswordView, UserLogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('changepassword/', UserChangePasswordView.as_view()),
    path('sent-password-reset-email/', SendPasswordResetEmailView.as_view()),
    path('reset-password/<uid>/<token>/', UserResetPasswordView.as_view())
]
