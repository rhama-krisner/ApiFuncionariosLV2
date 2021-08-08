from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ModelFuncionarios
from .serializer import FuncionariosSerializer

class AllFuncionarios(APIView):
    def get(self, request):
        funcionarios = ModelFuncionarios.objects.all()
        funcionariosSerializer = FuncionariosSerializer(funcionarios, many=True)
        return Response(funcionariosSerializer.data)

class AddFuncionario(APIView):
    def post(self, request):
        data = {
            'nome':request.data.get('nome'),
            'rg':request.data.get('rg'),
            'orgaoEmissor':request.data.get('orgaoEmissor'),
            'cpf':request.data.get('cpf'),
            'nacionalidade':request.data.get('nacionalidade'),
            'endereco':request.data.get('endereco'),
            'cep':request.data.get('cep'),
            'cidade':request.data.get('cidade'),
            'estado':request.data.get('estado'),
            'dataNascimento':request.data.get('dataNascimento'),
            'sexo':request.data.get('sexo'),
            'escolaridade':request.data.get('escolaridade')
        }

        funcionariosSerializer = FuncionariosSerializer(data=data)

        if funcionariosSerializer.is_valid():
            funcionariosSerializer.save()
            return Response(funcionariosSerializer.data)
        else:
            return Response(funcionariosSerializer.errors)

class FuncionarioGetPutDelete(APIView):
    def getFuncionarios(self, id):
        try:
            return ModelFuncionarios.objects.get(id=id)
        except ModelFuncionarios.DoesNotExist:
            return Http404

    def get(self, request, id):
        funcionarios = self.getFuncionarios(id=id)
        funcionariosSerializer = FuncionariosSerializer(funcionarios)
        return Response(funcionariosSerializer.data)
    
    def delete(self, request, id):
        funcionarios = self.getFuncionarios(id=id)
        funcionarios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def  put(self, request, id):
        funcionarios = self.getFuncionarios(id=id)
        serializer = FuncionariosSerializer(funcionarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class FuncionariosByPosition(APIView):
    def get(self, request):
        funcionarios = ModelFuncionarios.objects.filter(position=position)
        funcionariosSerializer = FuncionariosSerializer(funcionarios, many=True)
        return Return(funcionariosSerializer.data)

