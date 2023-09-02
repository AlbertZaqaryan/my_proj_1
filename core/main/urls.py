from django.urls import path
from . import views

urlpatterns=[
    path('', views.hello),
    path('calculator/', views.calculator)
]