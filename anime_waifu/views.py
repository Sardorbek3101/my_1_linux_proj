from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from anime_waifu.forms import UserCreateForm
from anime_waifu.models import CustomUSer


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
    

class UserRegisterView(View):
    def get(self, request):
        return render(request, "user_reg.html", {"form":UserCreateForm()})
    def post(self, request):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return(redirect('home'))
        else:
            context = {
                "form" : form
            }
            return render(request, "home.html", context)
        

class UserLoginView(View):
    def get(self, request):
        return render(request, "login.html", {"form":AuthenticationForm()})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"form":form})
            

class ProfileView(View):
    def get(self, request, username):
        try:
            user = CustomUSer.objects.get(username=username)
        except:
            raise Http404("Страница не найдена.")
        return render(request, "profile.html", {"user":user})