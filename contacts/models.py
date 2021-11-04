from django.db import models

# Create your models here.
class Contacts(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome