# Generated by Django 2.1.3 on 2018-12-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0004_auto_20181213_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='Perfil_interesse',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
