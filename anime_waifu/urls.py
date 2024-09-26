from django.urls import path
from anime_waifu.views import HomeView, UserRegisterView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('register/', UserRegisterView.as_view(), name="user_reg"),
]
