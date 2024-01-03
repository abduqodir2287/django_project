from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("members.urls")),
    path('admin/', admin.site.urls)
]
