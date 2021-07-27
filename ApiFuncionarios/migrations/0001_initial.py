# Generated by Django 3.2.5 on 2021-07-27 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFuncionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('rg', models.CharField(max_length=255)),
                ('orgaoEmissor', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('dataNascimento', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=255)),
                ('escolaridade', models.CharField(max_length=255)),
            ],
        ),
    ]
