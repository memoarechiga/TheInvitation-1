from django.db import models
from django.contrib.auth.models import User
from PIL import Image

PAQUETES_CHOISES = [     
        ('PREMIUM', 'Premium'),
        ('GOLD', 'Gold'),
        ('SILVER', 'Silver'),
        ('BASICO', 'Basico'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='avatar.jpg', # default avatar
        upload_to='profile_avatars' # dir to store the image
        )
    paquete = models.CharField(max_length=20, default= 'Basico', choices=PAQUETES_CHOISES)
    fecha_evento = models.DateField(null=True, blank=True)
    lugar_fiesta = models.CharField(max_length=100, null=True, blank=True)
    lugar_ceremonia = models.CharField(max_length=100, null=True, blank=True)
    festejados = models.CharField(max_length=100, null=True, blank=True)
    familiares1_festejados = models.CharField(max_length=200, null=True, blank=True)
    familiares1_foto = models.ImageField(upload_to='family_album', null=True, blank=True)
    familiares2_festejados = models.CharField(max_length=200, null=True, blank=True)
    familiares2_foto = models.ImageField(upload_to='family_album', null=True, blank=True)
    testigos_festejados = models.CharField(max_length=200, null=True, blank=True)
    codigo_vestimenta = models.CharField(max_length=100, null=True, blank=True)
    mesa_regalos = models.CharField(max_length=100, null=True, blank=True)
    link_regalos = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    template_invitacion = models.IntegerField(null=True, blank=True)
    pagado = models.BooleanField(default=False)
    ref_pago = models.BigIntegerField(unique=True, null=True, blank=True)

    
    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse("invitation", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)
            


           