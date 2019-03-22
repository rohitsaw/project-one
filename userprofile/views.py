from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Myuser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout


def index(request):
    if not request.user.is_authenticated:
        return render(request, "userprofile/login.html")
    try :
        myuser = Myuser.objects.get(user = request.user)
        context = {
        'user' : User.objects.get(username=request.user),
        'myuser': Myuser.objects.get(user=request.user),
        'flag': True
        }
        return render(request, "userprofile/profile.html", context)

    except Myuser.DoesNotExist:
        context = {
            'user' : User.objects.get(username=request.user),
            'flag' : False
            }
        return render(request, "userprofile/profile.html", context)


def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            #index(request)
            return HttpResponseRedirect(reverse("home:homepage"))
        return render(request, "userprofile/login.html", {"msg":"Invalid Credentials"})
    return render(request, "userprofile/login.html")

def logout(request):
    if (request.user.is_authenticated):
        auth_logout(request)
    return HttpResponseRedirect(reverse("home:homepage"))

def registration(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("userprofile:index"))
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        try:
            userexist = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            # myuser = Myuser(user = user)
            # myuser.save()
            return HttpResponseRedirect(reverse("userprofile:index"))
        return render(request, "userprofile/registration.html", {"msg":"Username already exist."})
    return render(request, "userprofile/registration.html")

def edit(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("userprofile:index"))
    if request.method == "POST":
        try:
            myuser = Myuser.objects.get(user = request.user)
        except Myuser.DoesNotExist:
            myuser = Myuser(user = request.user)
            myuser.save()
            myuser = Myuser.objects.get(user = request.user)


        myuser.name = request.POST['name']
        myuser.dob = request.POST['dob']
        myuser.email = request.POST['email']
        myuser.bio = request.POST['bio']
        myuser.qualification = request.POST['qualification']
        if 'photo' in request.FILES.keys():
            myuser.photo = request.FILES['photo']
        myuser.save()
        #print(request.user.myuser.key)
        return HttpResponseRedirect(reverse("userprofile:index"))
    if request.method == "GET":
        try:
            myuser = Myuser.objects.get(user = request.user)
            context = {'myuser': myuser}
            print("-------------------------------")
        except Myuser.DoesNotExist:
            context = {'myuser': request.user}
    return render(request, "userprofile/edit.html", context)
