from django.urls import path
from ApiFuncionarios import views

urlpatterns=[
    path('funcionarios/',views.AllFuncionarios.as_view(), name='funcionarios'),
    path('add/', views.AddFuncionario.as_view()),
    path('<int:id>/',views.FuncionarioGetPutDelete.as_view())
]