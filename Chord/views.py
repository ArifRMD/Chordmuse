from django.shortcuts import render, redirect
from multiprocessing import context
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from Chord.models import *

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

def Admin(request):
    template_name = "back/extended.html"
    context = {
        'title' : 'dashboard',
    }
    return render(request, template_name, context)


@login_required
@user_passes_test(is_operator)
def Table(request):
    template_name = "back/extended.html"
    Chord_list = chord.objects.all()

    context = {
        'title' : 'Table',
        'Chord' : Chord_list
    }
    return render(request, template_name, context)
    
@login_required
def Table_user(request):
    template_name = "back/User_table.html"
    user_list = User.objects.all()

    context = {
        'title' : 'Table user',
        'user_list' : user_list
    }
    return render(request, template_name, context)
    

@login_required
def Form(request):
    template_name = "back/regular.html"
    kat = Kategori.objects.all()
    if request.method == "POST":
            songname = request.POST.get('songname')
            date = request.POST.get('date')
            body = request.POST.get('body')
            kat = request.POST.get('kategori')
            kate = Kategori.objects.get(nama=kat)
            chord.objects.create(
                songname = songname,
                date = date,
                body = body,
                kategori = kate,
            )
            return redirect(Table)
            print(songname,date,body,kat)

    context = {
        'title':'Add Chord',
        'kategori': kat
    }
    return render(request,template_name,context)
    
@login_required
def edit_chord(request, id):
    template_name = "back/edit_chord.html"
    a = chord.objects.get(id=id)
    if request.method == "POST":
        
        songname = request.POST.get("songname")
        date = request.POST.get("date")
        body = request.POST.get("body")
        
        a.songname = songname
        a.date = date
        a.body = body
        a.save()
        return redirect(Table)
    context = {
        'title':'edit Chord',
        'chord' : a,
    }
    return render(request,template_name,context)

@login_required
def edit_User(request, id):
    template_name = "back/edit_User.html"
    U = User.objects.get(id=id)
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        
        U.songname = username
        U.date = password
        U.body = email
        U.save()
        return redirect(Table_user)
    context = {
        'title':'edit Chord',
        'chord' : U,
    }
    return render(request,template_name,context)

@login_required
def lihat_User(request, id):
    template_name = "back/detail_user.html"
    User = User.objects.get(id=id)
    context= {
        'title' : 'lihat User',
        'User' : User,

    }
    return render(request, template_name, context)

@login_required
def lihat_chord(request, id):
    template_name = "back/detail.html"
    Chord = chord.objects.get(id=id)
    context= {
        'title' : 'lihat Chord',
        'chord' : Chord,

    }
    return render(request, template_name, context)
@login_required
def delete_chord(request, id):
    chord.objects.get(id=id).delete()
    return redirect(Table)
