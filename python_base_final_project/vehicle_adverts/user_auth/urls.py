from django.urls import path
from django.views.generic import TemplateView
from .views import LoginView, LogoutView, RegisterView

app_name = "user_auth"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login",),
    path("logout/", LogoutView.as_view(), name="logout",),
    path("register/", RegisterView.as_view(), name="register",),
    path("profile/", TemplateView.as_view(template_name="user_auth/user-profile.html"), name="user-profile")

]
