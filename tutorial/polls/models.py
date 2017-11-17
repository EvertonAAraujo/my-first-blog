from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length= 50)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Teste(models.Model):
    numero = models.CharField(max_length=10)
    nome = models.CharField(max_length=200)


    def __str__(self):
        return self.nome

@python_2_unicode_compatible
class Pergunta(models.Model):
    pergunta_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pergunta_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    escolha_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.escolha_text