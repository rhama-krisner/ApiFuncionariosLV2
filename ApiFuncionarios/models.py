from django.db import models

# Create your models here.

class ModelFuncionarios(models.Model):
    sexoChoice = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Nenhuma das opções')
    )

    nome = models.CharField(max_length=255)
    rg = models.IntegerField(max_length=8)
    orgaoEmissor = models.CharField(max_length=255)
    cpf = models.IntegerField(max_length=11)
    nacionalidade = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    dataNascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=sexoChoice, blank=False, null=False)
    escolaridade = models.CharField(max_length=255)
    email = models.EmailField(max_length = 255, default = 'Nulo')

    def __str__(self):
        return self.nome