from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.

CATEGORY_CHOISES = [     
        ('FIESTA', 'Fiesta'),
        ('EVENTO', 'Evento'),
        ('INFANTIL', 'Infantil'),
]

class UserGallery(models.Model):
    photo = models.FileField(upload_to='user_gallery', max_length=100)
    description = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description

class InvitationCatalog(models.Model):
    example = models.ImageField(upload_to='invitation_catalog')
    catalog_name = models.CharField(max_length=100)
    description = models.CharField(max_length=180)
    category = models.CharField(max_length=20, default='Fiesta', choices=CATEGORY_CHOISES)
    
    def __str__(self):
        return self.catalog_name



