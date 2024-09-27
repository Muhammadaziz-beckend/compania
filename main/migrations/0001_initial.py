# Generated by Django 5.0.6 on 2024-07-09 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catigori_woork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Названия катигория')),
            ],
            options={
                'verbose_name': 'Катигория',
                'verbose_name_plural': 'Катигории',
            },
        ),
        migrations.CreateModel(
            name='Sotrudnic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Woor', verbose_name='Изображения сотрудника')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('jod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sotrudnnic', to='main.catigori_woork')),
            ],
            options={
                'verbose_name': 'Сатрудник',
                'verbose_name_plural': 'Сатрудники',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображения')),
                ('name', models.CharField(max_length=65, verbose_name='Названия задания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_end', models.DateTimeField(auto_now_add=True, verbose_name='Срок до')),
                ('who_develops', models.ManyToManyField(to='main.sotrudnic')),
            ],
            options={
                'verbose_name': 'Зада́ние',
                'verbose_name_plural': 'Зада́ния',
            },
        ),
    ]