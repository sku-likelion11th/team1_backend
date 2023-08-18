from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    # index.html(기본화면) 올려주기
    path("", views.home, name="home"),
    
    #로그인 관련된 url 정리
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path('myPlayer/<username>/', views.myplayer_view, name='myplayer_view'),
    path('nonePlayer/<username>/', views.myplayer_view, name='noneplayer_view'),
    
    #post 관련 url정리 
    path('writing/<username>/', views.create_post, name="writing"),
]