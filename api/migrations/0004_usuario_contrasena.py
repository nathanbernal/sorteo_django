# Generated by Django 3.1.9 on 2021-05-19 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_usuario_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
