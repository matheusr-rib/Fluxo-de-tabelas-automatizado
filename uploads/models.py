from django.db import models

# Create your models here.
class Upload(models.Model):
    arquivo = models.FileField(upload_to='')
    criado_em = models.DateTimeField(auto_now_add=True)