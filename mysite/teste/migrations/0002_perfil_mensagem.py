# Generated by Django 2.1.4 on 2018-12-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='mensagem',
            field=models.CharField(default='va se foder', max_length=100),
        ),
    ]
