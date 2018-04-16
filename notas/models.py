from _pydecimal import Decimal
from typing import Any, Union

from django.db import models
from decimal import Decimal
# Create your models here.
class Avaliador (models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return str(self.nome)


class Autor (models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return str(self.nome)

@property
class Avaliacao(models.Model):
    avaliador=models.ForeignKey('Avaliador', on_delete=models.CASCADE)
    qualidade_técnica = models.DecimalField(max_digits=2, decimal_places=1)
    inovacao = models.DecimalField(max_digits=2, decimal_places=1)
    resultados = models.DecimalField(max_digits=2, decimal_places=1)
    metodologia = models.DecimalField(max_digits=2, decimal_places=1)
    adequacao = models.DecimalField(max_digits=2, decimal_places=1)
    def calcMedia(self):
        from decimal import Decimal
        media = ((self.qualidade_técnica or 0) + (self.inovacao or 0) + (self.resultados or 0) + (self.metodologia or 0) + (self.adequacao or 0)) / Decimal(5)
        return media

    media = models.DecimalField(nota,max_digits=2, decimal_places=1,editable=False)


class Artigo(models.Model):
    autor= models.ManyToManyField('Autor')
    titulo = models.CharField(max_length=120)
    avaliacao = models.ForeignKey('Avaliacao', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.titulo)

    