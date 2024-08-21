from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.app_view, name='app_view'),
    path('afficheur', views.afficheur_view, name='afficheur_view'),
    path('add-rdv/', views.add_rdv, name='add-rdv'),
    path('delete-rdv/', views.delete_rdv, name='delete-rdv'),
]
