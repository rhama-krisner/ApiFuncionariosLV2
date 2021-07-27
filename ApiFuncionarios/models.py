from django.db import models

# Create your models here.

class ModelFuncionarios(models.Model):
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=255)
    orgaoEmissor = models.CharField(max_length=255)
    cpf = models.CharField((max))
    nacionalidade = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    dataNascimento = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    escolaridade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome