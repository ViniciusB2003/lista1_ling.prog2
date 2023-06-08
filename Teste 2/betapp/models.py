from django.db import models

# Create your models here.
class Teste(models.Model):
    nome_text = models.CharField(max_length=200)

