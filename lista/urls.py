from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend, name="frontend"),
    path('register/', views.register_request, name="register"),
    path('dodaj/', views.dodaj, name="dodaj"),
    path('dodajprojekt/', views.dodaj_projekt, name="dodaj_projekt"),
    path('edit/<str:id>/', views.edit, name="edit"),
    path('editprojekt/<str:id>/', views.edit_projekt, name="edit_projekt"),
    path('delete/<str:id>/', views.delete, name="delete"),
    path('deleteprojekt/<str:id>/', views.delete_projekt, name="delete_projekt"),
]