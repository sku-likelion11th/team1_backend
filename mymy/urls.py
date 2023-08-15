from django.contrib import admin
from django.urls import include, path

#Project 폴더에서 urls.py정리해주면 깔끔.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('accounts.urls')),
]