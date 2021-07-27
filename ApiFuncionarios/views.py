from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ModelFuncionarios
from .serializer import FuncionariosSerializer


