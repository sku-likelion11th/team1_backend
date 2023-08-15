from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
path("admin/", admin.site.urls),
path("signup/", views.signup, name="signup"),
path("signin/", views.signin, name="signin"),
path("", views.home, name="home"),
path('myPlayer/<username>/', views.myplayer_view, name='myplayer_view'),
# path('logout/', views.signout, name='logout'),
path("nonePlayer/", views.noneplayer_view, name="nonePlayer_view"),
path("writing/", views.writing_view, name="writing_view"),

]
