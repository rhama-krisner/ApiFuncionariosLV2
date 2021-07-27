from rest_framework import serializer
from ApiFuncionarios.models import ModelFuncionarios

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelFuncionarios
        fields = '__all__'