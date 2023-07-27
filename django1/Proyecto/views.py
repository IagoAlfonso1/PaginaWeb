from django.shortcuts import render, redirect
from .models import Persona, PersonaForm, Jugador,Equipo
from django.views import View

class PersonaNueva(View):
    template_name = 'main/Template1.html'

    def get(self, *args, **kwargs):

        context = {}

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = PersonaForm(self.request.POST)

        if form.is_valid():

            nueva_persona = Persona()
            nueva_persona.nombre = form.cleaned_data['nombre']
            nueva_persona.apellido = form.cleaned_data['apellido']
            nueva_persona.DNI = form.cleaned_data['DNI']
            nueva_persona.NombreEquipo = form.cleaned_data['NombreEquipo']
            nueva_persona.contra = form.cleaned_data['contra']

            nueva_persona.save()
            return redirect('main:iniciosesion')
        else:
            return render(self.request, self.template_name, {'form': form})

class InicioSesion(View):
    template_name = 'main/InicioSesion.html'
    form = PersonaForm(initial={'DNI': Persona.DNI, 'Contraseña': Persona.contra})
    def get(self, *args, **kwargs):
        context = {}
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):

        return redirect('main:Lobby')

class Principal(View):
    template_name = 'main/Lobby.html'

    def get(self, *args, **kwargs):
        jugadores = Jugador.objects.all()
        context = {'jugadores': jugadores}

        return render(self.request, self.template_name,context)
    def post(self, *args, **kwargs):

            return  redirect('main:iniciosesion')


class JugadoresList(View):
    model = Jugador
    template_name = 'main/Jugadores.html'
    def get(self, *args, **kwargs):
        jugadores = Jugador.objects.all()
        context = {'jugadores': jugadores}

        return render(self.request, self.template_name,context)
    def post(self, *args, **kwargs):

            return  redirect('main:iniciosesion')


class Tabla(View):
    template_name = 'main/Tabla.html'
    def get(self, *args, **kwargs):
        equipo = Equipo.objects.all()
        persona = Persona.objects.all()
        context = {'equipos': equipo, 'personas': persona}
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        return redirect('main:iniciosesion')

class index(View):
    template_name = 'main/index.html'
    def get(self, *args, **kwargs):

        context = {}

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):

        return redirect('main:InicioSesion')


