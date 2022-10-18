from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from users.models import *
from django.views import View
from django.shortcuts import get_object_or_404


def registration(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid(): #запускает все наши валидации и если ни одна ошибка не рейзнулась, то форма считается валидной.
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/registration_done.html', {'new_user' : new_user})
        return render(request, 'accounts/registration.html', {'user_form' : user_form})
    
    user_form = UserRegistrationForm()  
    return render(request, 'accounts/registration.html', {'user_form' : user_form})

class Profile(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')