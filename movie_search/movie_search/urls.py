"""
URL configuration for movie_search project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path
from moviesss.views import movie_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', movie_search, name='movie_search'),
]
