from core import views
from django.urls import path

urlpatterns = [
    path('greeting/', views.greeting),
    path('hello/', views.hello),
    path('present', views.present),
]