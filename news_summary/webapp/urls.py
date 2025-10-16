from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_titles/', views.get_titles, name='get_titles'),
    path('get_article_using_title/', views.get_article_using_title, name='get_article_using_title'),
    path('get_article_using_url/', views.get_article_using_url, name='get_article_using_url'),
    path('get_extractive/', views.get_extractive, name='get_extractive'),
    path('get_abstractive/', views.get_abstractive, name='get_abstractive'),
]
