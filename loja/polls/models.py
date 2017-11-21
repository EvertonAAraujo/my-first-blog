import datetime
import re

from localflavor.br.forms import phone_digits_re, cpf_digits_re

from django.db import models
from django.utils import timezone
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Field, RegexField, Select
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from localflavor.compat import EmptyValueCompatMixin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    telefone = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    produto = models.CharField(max_length=200)
    preco = models.IntegerField()
    def __str__(self):
        return self.produto


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nome

    @property
    def valor(self):
        return self.produto.preco * self.quantidade
