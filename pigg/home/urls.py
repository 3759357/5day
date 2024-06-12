from django.urls import path
from . import views
from .views import *
urlpatterns=[
    path('',views.main_feed),
    path('history/', views.history),
    path('story/',views.story),
    path('style/',views.style),
    path('menu/', views.menu),
    path('restaurant/', views.restaurant),
    path('franchise_story/', views.franchise_story),
    path('franchise/', views.franchise),
    path('review/', views.review),
    path('index/',views.index),
    path('blog/',views.blog),
    path('blog/<int:pk>/',views.posting, name="posting"),
    path('story/<int:pk>/',views.posting, name="posting"),
    path('review/send/', views.send_email),
]