from django.urls import path
from anime_waifu.views import HomeView, UserRegisterView, UserLoginView, ProfileView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('register/', UserRegisterView.as_view(), name="user_reg"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('<str:username>/', ProfileView.as_view(), name="profile")
]
