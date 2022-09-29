from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #IP 주소/blog/
    path('<int:pk>/', views.single_post_page),
]