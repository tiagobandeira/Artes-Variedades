from django.db import models
from django.utils import timezone

# Create your models here.
class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.FloatField()
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publica(self):
        self.data_publicacao = timezone.now()
        self.save()
    def __str__(self):
        return self.titulo
    
