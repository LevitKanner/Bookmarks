from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('details/<int:id>/<slug:slug>/', views.image_detail, name='image_detail'),
    path('like/', views.image_like, name='like')
    ]