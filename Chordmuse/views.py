from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from Chord.models import *

def home(request):
    template_name = 'front/index.html'
    Chord_list = chord.objects.all()
    context = {
        'title':'my home',
        'chord' : Chord_list,
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/aboutus.html'
    context = {
        'title':'About',
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)

def create(request):
    template_name = "front/Create User.html"
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            User.objects.create(
                username = username,
                password = password,
                email = email,

            )
            return redirect(Login)
            print(username,password,email)

    context = {
        'title':'Add Chord',
    }
    return render(request,template_name,context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    template_name = 'front/login-page.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request,user)
        else:
            print('username salah')
    context = {
        'title':'Login',
    }
    return render(request, template_name, context)

def logout_admin(request):
    logout(request)
    return redirect('home')

def Detail_chord(request, id):
    template_name = "front/Detail_chord.html"
    Chord = chord.objects.get(id=id)
    context= {
        'title' : 'lihat Chord',
        'chord' : Chord,

    }
    return render(request, template_name, context)

def POP(request):
    template_name = 'front/POP.html'
    Chord = chord.objects.all()
    context= {
        'title' : 'lihat Chord',
        'chord' : Chord,
    }
    return render(request, template_name, context)

def ROCK(request):
    template_name = 'front/ROCK.html'
    Chord = chord.objects.all()
    context= {
        'title' : 'lihat Chord',
        'chord' : Chord,
    }
    return render(request, template_name, context)

def JAZZ(request):
    template_name = 'front/JAZZ.html'
    Chord = chord.objects.all()
    context= {
        'title' : 'lihat Chord',
        'chord' : Chord,
    }
    return render(request, template_name, context)

def REAGGEA(request):
    template_name = 'front/REAGGEA.html'
    Chord = chord.objects.all()
    context= {
        'title' : 'lihat Chord',
        'chord' : Chord,
    }
    return render(request, template_name, context)

def PUNK(request):
    template_name = 'front/PUNK.html'
    Chord = chord.objects.all()
    context= {
        'title' : 'lihat Chord',
        'chord' : Chord,
    }
    return render(request, template_name, context)
