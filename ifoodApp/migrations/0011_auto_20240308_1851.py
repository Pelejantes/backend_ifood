# Generated by Django 3.2.5 on 2024-03-08 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0010_auto_20240307_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='codVerif',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contaBancariaId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.contabancaria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagemPerfil',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nomeUsu',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefoneUsu',
            field=models.CharField(max_length=14, null=True),
        ),
    ]