# Generated by Django 3.2.9 on 2022-01-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=50)),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]