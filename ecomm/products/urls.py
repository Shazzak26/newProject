from django.urls import path
from . import views

urlpatterns = [
    path('cat_create',views.cat_create, name='cat-create'),
    path('index/', views.index, name='index'),
    path('',views.home, name='home'),
]
