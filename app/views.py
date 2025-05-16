from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse
from .models import RegistrationLinks
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import transaction

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
                                email=cd['email'], 
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Login is success")
                else:
                    return HttpResponse('Data is inactive')
            else:
                return HttpResponse('Data is incorrect')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def register_view(request, token):
    registration_link  = RegistrationLinks.objects.filter(token=token, used=False).first()
    if not registration_link :
        return HttpResponse('Link is invalid\n' \
            'Contact the administrator to receive a registration link.')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    cd = form.cleaned_data
                    User.objects.create_user(username=cd['username'],
                                             email=cd['email'],
                                             password=cd['password'])
                    registration_link.used = True
                    registration_link.save()

                    return HttpResponse('Register is success')

            except Exception as e:
                return HttpResponse("Error")
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form, 'token': token})
        