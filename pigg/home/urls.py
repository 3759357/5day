from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from pigg import settings
from . import views
from django.contrib import admin

from .views import *
urlpatterns=[
    path('', views.main_feed),
    path('history/', views.history),
    path('story/', views.story),
    path('style/', views.style),
    path('menu/', views.menu),
    path('restaurant/', views.restaurant),
    path('franchise_story/', views.franchise_story),
    path('franchise/', views.franchise),
    path('review/', views.review),
    path('index/', views.index),
    path('blog/', views.blog),
    path('blog/<int:pk>/', views.posting, name="posting"),
    path('story/<int:pk>/', views.posting, name="posting"),
    path('review/send/', views.send_email),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
