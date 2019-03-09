from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField('titulo', max_length=128)
    conteudo = models.TextField()
    data_criacao = models.DateField()
    data_publicacao = models.DateTimeField()
    publicado = models.BooleanField()
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    