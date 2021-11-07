from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'curso'
    
    def __str__(self):
        return self.nome