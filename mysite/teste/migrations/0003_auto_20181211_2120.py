# Generated by Django 2.1.4 on 2018-12-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0002_perfil_mensagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='mensagem',
        ),
        migrations.AddField(
            model_name='perfil',
            name='perfil_mensagem',
            field=models.CharField(default='', max_length=100),
        ),
    ]