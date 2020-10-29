from dj_rest_auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users.views import FacebookLogin, UserMeView

app_name = "users"
urlpatterns = [
    path("auth/login/", FacebookLogin.as_view(), name="facebook-login"),
    path("auth/refresh_token/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("me/", UserMeView.as_view(), name="me-detail"),
]
