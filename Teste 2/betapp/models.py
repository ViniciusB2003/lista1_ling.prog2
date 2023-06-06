from django.db import models

# Create your models here.
class Principal(models.Model):
    descricao_text = models.CharField(max_length=200)
    nome_text = models.CharField(max_length=200)

