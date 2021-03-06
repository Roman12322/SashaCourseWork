# Generated by Django 4.0.2 on 2022-02-04 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('sqn1', models.CharField(max_length=100)),
                ('sqn2', models.CharField(max_length=100)),
                ('result', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
