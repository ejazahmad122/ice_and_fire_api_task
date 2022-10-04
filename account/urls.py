from django.urls import path, include
from .views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserResetPasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('changepassword/', UserChangePasswordView.as_view()),
    path('sent-password-reset-email/', SendPasswordResetEmailView.as_view()),
    path('reset-password/<uid>/<token>/', UserResetPasswordView.as_view())
]
