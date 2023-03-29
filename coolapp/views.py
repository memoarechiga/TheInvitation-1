from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import UserGallery, InvitationCatalog
from users.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

### Galeria de Usuarios ### -inicio

class UserGalleryList(LoginRequiredMixin, ListView):
    model = UserGallery
    context_object_name = 'usergallery'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usergallery'] = context['usergallery'].filter(user=self.request.user)
        return context

class UserGalleryDetail(LoginRequiredMixin, DetailView):
    model = UserGallery
    context_object_name = 'usergallerydetail'

### Galeria de Usuarios ### -end

class UserPayment(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'userpayment'
    template_name = 'payment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userpayment'] = context['userpayment'].filter(user=self.request.user)
        return context




### Vistas de Catalogos de Invitaciones## -inicio

class InvitationCatalogList(ListView):
    model = InvitationCatalog
    context_object_name = 'invitationcatalog'
    template_name = 'catalogo.html'

class InvitationCatalogFiesta(ListView):
    model = InvitationCatalog
    context_object_name = 'catalogofiesta'
    template_name = 'catalogo_fiestas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["catalogofiesta"] = InvitationCatalog.objects.filter(category__contains='Fiesta')
        return context

class InvitationCatalogEvento(ListView):
    model = InvitationCatalog
    context_object_name = 'catalogoevento'
    template_name = 'catalogo_evento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["catalogoevento"] = InvitationCatalog.objects.filter(category__contains='Evento')
        return context

class InvitationCatalogInfantil(ListView):
    model = InvitationCatalog
    context_object_name = 'catalogoinfantil'
    template_name = 'catalogo_infantil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["catalogoinfantil"] = InvitationCatalog.objects.filter(category__contains='Infantil')
        return context

### Vistas de Catalogos de Invitaciones## -end



### Templates de Invitaciones ### -inicio

class UserInvitation(DetailView):
    model = Profile
    context_object_name = 'userinvitation'
    template_name = "invitation.html"
    pk_url_kwarg = "profile_id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

class UserInvitation1(DetailView):
    model = Profile
    context_object_name = 'userinvitation'
    template_name = "invitation1.html"
    pk_url_kwarg = "profile_id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

### Templates de Invitaciones ### -end

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contacto.html')

def paquetes(request):
    return render(request, 'paquetes.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



