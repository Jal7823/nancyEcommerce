from django.contrib import admin
from django.urls import path, include
from .views import LoginFromView,LogoutView,formulario,registro,UserProfile

urlpatterns = [
    path('', LoginFromView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/',formulario, name='registro'),
    path('perfil/<int:pk>',UserProfile.as_view(), name='perfil'),
]

