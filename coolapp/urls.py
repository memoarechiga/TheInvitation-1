from django.urls import path
from .views import (UserGalleryList, index, dashboard, UserGalleryDetail, about, 
                    contacto, InvitationCatalogList, InvitationCatalogFiesta, 
                    InvitationCatalogEvento, InvitationCatalogInfantil, paquetes, 
                    UserInvitation, UserInvitation1, UserPayment)

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('gallery/', UserGalleryList.as_view(), name='usergallery'),
    path('gallerydetail/<int:pk>/',UserGalleryDetail.as_view(),name='usergallerydetail'),
    path('about/', about, name='about'),
    path('paquetes/', paquetes, name='paquetes'),
    path('contacto/', contacto, name='contacto'),
    path('catalogo/', InvitationCatalogList.as_view(), name='catalogo'),
    path('catalogo_fiesta/', InvitationCatalogFiesta.as_view(), name='catalogofiesta'),
    path('catalogo_evento/', InvitationCatalogEvento.as_view(), name='catalogoevento'),
    path('catalogo_infantil/', InvitationCatalogInfantil.as_view(), name='catalogoinfantil'),
    path('payment/', UserPayment.as_view(), name='userpayment'),

    path('invitacion1/<slug:slug>/', UserInvitation.as_view() ,name='userinvitation1'),
    path('invitacion2/<slug:slug>/', UserInvitation1.as_view() ,name='userinvitation2'),
]
