from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .models import User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

class RegistrationView(View):
    def get(self, request):
        return render(request, 'registration/registration.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            if User.objects.get(username=username, password=password, email=email):
                return redirect('home')  # пользователь уже существует отправляем на страничку home
        except ObjectDoesNotExist:
            User.objects.create(username=username, password=password, email=email)
            return redirect('login')  # Перенаправление на страницу входа
        except MultipleObjectsReturned:
            User.objects.create(username=username, password=password, email=email)
            return redirect('login')  # Перенаправление на страницу входа

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            if User.objects.get(username=username) and User.objects.get(password=password):
                return redirect('home')
            else:
                return redirect('register')
        except ObjectDoesNotExist:
            return redirect('register')
        except MultipleObjectsReturned:
            return redirect('register')


class HomeView(View):
    def get(self, request):
        return render(request, 'registration/home.html')

class ProfileView(View):
    def get(self, request):
        return render(request, 'registration/profile.html')

class HuiVrot(View):
    def get(self, request):
        return render(request, 'registration/home.html')




