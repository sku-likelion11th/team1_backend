from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView
from django.dispatch import receiver
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignInForm, SignUpForm
from .models import User, Post



def home(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "GET":
        form = SignUpForm()

    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")  # 사용자 입력 필드 이름에 맞게 변경
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("myplayer_view", username=user.username)
            else:
                messages.error(request, "Invalid user ID or password")
                print("Authentication failed")

    else:
        form = AuthenticationForm()

    return render(request, "accounts/index.html", {"form": form})


def create_post(request):
    post=Post()
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content'] 
        post.created_at = datetime.now()       
        post.save()
        return redirect('/post/')
    return render(request, "accounts/writing.html")




@login_required  # 로그인 상태를 확인하는 데코레이터
def myplayer_view(request, username):
    user = request.user  # 현재 로그인된 사용자 정보를 가져옵니다.
    posts = Post.objects.filter(user=user)
    return render(request, "accounts/myPlayer.html", {"user": user, "posts": posts})

def noneplayer_view(request):
    return render(request, "accounts/nonePlayer.html")
    # 불특정 다수 페이지
    