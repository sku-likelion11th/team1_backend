from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import SignInForm, SignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm



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
                return redirect("myPlayer_view")
            else:
                messages.error(request, "Invalid user ID or password")
                print("Authentication failed")

    else:
        form = AuthenticationForm()

    return render(request, "accounts/index.html", {"form": form})


@login_required  # 로그인 상태를 확인하는 데코레이터
def myplayer_view(request):
    # 이 뷰 함수에서 원하는 로직을 추가하세요.
    # 사용자가 로그인된 상태이므로 로직을 작성할 수 있습니다.
    # 예: 특정 정보를 불러와서 템플릿에 전달하거나, 다른 작업을 수행하십시오.

    return render(request, "accounts/myPlayer.html")

def noneplayer_view(request):
    return render(request, "accounts/nonePlayer.html")
    # 불특정 다수 페이지
    
def writing_view(request):
    return render(request, "accounts/writing.html")
    #불특정 다수가 테이프 만들기 버튼 눌렀을 때



# User 모델에 대한 post_save 수신기 작성
# @receiver(post_save, sender=User)
# def create_post(sender, instance, created, **kwargs):
#     if created:
#         Post.objects.create(user=instance)

# class PostListView(ListView):
#     model = Post
#     template_name = 'mymyapp/post_list.html'
#     context_object_name = 'posts'
#     ordering = ['-created_at']

# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'myapp/signup.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return HttpResponseRedirect(reverse_lazy('post_detail', args=[user.post.post_number]))

# class PostDetailView(generic.DetailView):
#     model = Post
#     template_name = 'myapp/post_detail.html'

#     # 댓글 작성에 사용할 폼을 context에 추가
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form'] = CommentForm()
#         return context

#     # 댓글 작성 기능
#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)

#         if form.is_valid():
#             comment = form.save(commit=False)
#         if request.user.is_authenticated:
#             comment.writer = request.user
#         else:
#             comment.writer = None
#         comment.post = self.get_object()
#         comment.save()

#         return HttpResponseRedirect(reverse('post_detail', args=[self.get_object().pk]))

#         return self.get(request, *args, **kwargs)
