from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Comment

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('user_id', 'nickname', 'password1', 'password2')

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content')


class SignUpForm(UserCreationForm):
    # SignUpForm 를 생성합니다.

    user_id = forms.CharField(max_length=150, help_text="Please enter your ID")
    # CharField는 문자열 데이터처리를 위한 입력 필드 형식, 최대길이 150자 설정, 도움말 텍스트는 양식의 입력 필드

    nickname = forms.CharField(max_length=20, help_text="Please enter your ID")
    # CharField는 문자열 데이터처리를 위한 입력 필드 형식, 최대길이 20자, 도움말 텍스트는 양식의 입력 필드

    password1 = forms.CharField(
        label="Password",
        max_length=20,
        widget=forms.PasswordInput(),
        help_text="Your password must contain at leeast 8 characters.",
    )
    # CharField는 문자열 데이터처리를 위한 입력 필드 형식, 최대길이 20자, 도움말 텍스트는 양식의 입력 필드

    password2 = forms.CharField(
        label="Password confirmation",
        max_length=20,
        widget=forms.PasswordInput(),
        help_text="Enter the same password as before, for verification.",
    )
    # CharField는 문자열 데이터처리를 위한 입력 필드 형식, 최대길이 20자, 도움말 텍스트는 양식의 입력 필드

    class Meta:
        model = User
        fields = ["user_id", "nickname", "password1", "password2"]


class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["user_id", "password"]
