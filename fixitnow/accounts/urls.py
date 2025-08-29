from django.urls import path
from .views import signup_view, login_view, logout_view, SignupView, LoginView, LogoutView

urlpatterns = [
   
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

   
    path("api/signup/", SignupView.as_view(), name="api-signup"),
    path("api/login/", LoginView.as_view(), name="api-login"),
    path("api/logout/", LogoutView.as_view(), name="api-logout"),
]
