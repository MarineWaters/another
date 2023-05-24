from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('template/<int:template_id>/', views.template, name='template'),
]