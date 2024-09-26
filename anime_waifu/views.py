from django.shortcuts import render, redirect
from django.views import View
from anime_waifu.forms import UserCreateForm


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