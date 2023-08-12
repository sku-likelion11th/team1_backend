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

# from .models import User, Post, Comment


def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "GET":
        form = SignUpForm()

    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    return render(request, "signup.html", {"form": form})


def signin(request):
    if request.method == "GET":
        form = SignInForm()
    elif request.method == "POST":
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, user_id=user_id, password=password)
            if user is not None:
                login(request, user)
                return redirect("myPlayer")
            else:
                messages.error(request, "Invalid username or password")

    return render(request, "signin.html", {"form": form})


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
