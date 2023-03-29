from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Profile
from coolapp.models import UserGallery
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views import View



class ProfileList(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profilelist'

class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profiledetail'
    template_name = 'users/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        context["users"] = User.objects.filter(pk=self.object.pk)
        return context
    

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_update.html'
    fields = [
        "slug",
        "ref_pago",
        "avatar",
        "festejados",
        "paquete",
        "fecha_evento",
        "lugar_fiesta",
        "lugar_ceremonia",
        "familiares1_festejados",
        "familiares1_foto",
        "familiares2_festejados",
        "familiares2_foto",
        "testigos_festejados",
        "codigo_vestimenta",
        "mesa_regalos",
        "link_regalos",
        "template_invitacion",
        "pagado",
    ]

    def get_success_url(self):
        return reverse_lazy('profiledetail', args=[self.object.pk])

    
class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            
        return super(RegisterView, self).form_valid(form)
    
    
class MyLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dashboard') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

            