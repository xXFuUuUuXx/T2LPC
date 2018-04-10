from django.db import models

# Create your models here.
class Avaliador (models.Model):
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def __str__(self):
        return str(self.nome)


class Autor (models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return str(self.nome)


class Avaliacao(models.Model):
    avaliador=models.ForeignKey('Avaliador', on_delete=models.CASCADE)
    qualidade_técnica = models.DecimalField(max_digits=2, decimal_places=1, min_value=0)
    inovacao = models.DecimalField(max_digits=2, decimal_places=1)
    resultados = models.DecimalField(max_digits=2, decimal_places=1, min_value=0)
    metodologia = models.DecimalField(max_digits=2, decimal_places=1)
    adequacao = models.DecimalField(max_digits=2, decimal_places=1)
    media =  models.DecimalField(max_digits=2, decimal_places=1)

class Artigo(models.Model):
    autor= models.ManyToManyField('Autor')
    titulo = models.CharField(max_length=120)
    avaliacao = models.ForeignKey('Avaliacao', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)
    #medias = calculo


#def calculo()
#   avaliacoes=Avaliacao.objects.all()