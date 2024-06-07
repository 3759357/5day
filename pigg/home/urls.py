from django.urls import path
from . import views

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
]