# Generated by Django 5.0.2 on 2024-03-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('surname', models.CharField(max_length=200, verbose_name='Surname')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('number', models.CharField(max_length=200, verbose_name='Phone number')),
                ('basket', models.TextField(max_length=200, verbose_name='Basket')),
            ],
        ),
    ]
