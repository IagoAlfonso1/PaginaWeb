from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'Proyecto'
urlpatterns = [
    path("", views.index.as_view(),name='Index'),
    path("Registrarse/", views.PersonaNueva.as_view(), name='Registrarse'),
    path("InicioSesion/", LoginView.as_view(template_name='main/InicioSesion.html'), name='iniciosesion'),
    path("Lobby/", views.Principal.as_view(), name="Lobby"),
    path('Lobby/Liga/', views.Tabla.as_view(), name='Liga'),
    path('Lobby/Coleccion/', views.JugadoresList.as_view(), name='coleecion'),
]