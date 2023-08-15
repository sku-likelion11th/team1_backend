from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Post



class SignUpForm(UserCreationForm):
    # SignUpForm 를 생성합니다.

    username = forms.CharField(max_length=20, help_text="ID를 입력하세요.")
    # CharField는 문자열 데이터처리를 위한 입력 필드 형식, 최대길이 20자 설정, 도움말 텍스트는 양식의 입력 필드

    nickname = forms.CharField(max_length=20, help_text="Please enter your NickName")
    # CharField는 문자열 데이터처리를 위한 입력 필드 형식, 최대길이 20자, 도움말 텍스트는 양식의 입력 필드

    password1 = forms.CharField(
        label="Password",
        max_length=20,
        widget=forms.PasswordInput(),
        help_text="비밀번호를 최소 8자 이상 입력하세요.",
    )
    # CharField는 문자열 데이터처리를 위한 입력 필드 형식, 최대길이 20자, 도움말 텍스트는 양식의 입력 필드

    password2 = forms.CharField(
        label="Password confirmation",
        max_length=20,
        widget=forms.PasswordInput(),
        help_text="다시 한 번 입력하세요.",
    )
    # CharField는 문자열 데이터처리를 위한 입력 필드 형식, 최대길이 20자, 도움말 텍스트는 양식의 입력 필드

    class Meta:
        model = User
        fields = ["username", "nickname", "password1", "password2"]


class SignInForm(AuthenticationForm):
    pass


class PostForm(forms.ModelForm):
    class Meta:
      model = Post
      fields = ('title','content')