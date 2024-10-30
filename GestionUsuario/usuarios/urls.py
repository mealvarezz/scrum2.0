from django.urls import path, include
from .import views
from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)

app_name = "usuarios"

urlpatterns = [
    path("registro/", views.register, name="register"),
    path("login/",
        views.CustomLoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
