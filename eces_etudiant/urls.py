from django.urls import path
from . import views
from .views import VoirEtu


urlpatterns = [
    path('', views.acceuil, name="acceuil"),
     path('acceuil/', views.acceuil, name="acceuil"),
    path('etudiant/',views.etudiant,name='etudiant'),
    path('voir_etudiant/<int:pk>',VoirEtu.as_view(),name='voir_etudiant'),




]
