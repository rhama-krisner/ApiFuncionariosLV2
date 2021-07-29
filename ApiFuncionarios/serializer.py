from rest_framework import serializers
from ApiFuncionarios.models import ModelFuncionarios

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelFuncionarios
        fields = '__all__'