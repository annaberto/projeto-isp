# Generated by Django 4.2.4 on 2024-10-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroIncidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cisp', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('sexo', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Não informado', 'Não informado')], max_length=50)),
                ('cor', models.CharField(choices=[('Negra', 'Negra'), ('Parda', 'Parda'), ('Amarela', 'Amarela'), ('Não informada', 'Não informada')], max_length=50)),
                ('idade', models.CharField(choices=[('18 a 59 anos', '18 a 59 anos'), ('60 anos ou mais', '60 anos ou mais'), ('Sem informação', 'Sem informação')], max_length=50)),
                ('vitimas', models.IntegerField()),
            ],
        ),
    ]
