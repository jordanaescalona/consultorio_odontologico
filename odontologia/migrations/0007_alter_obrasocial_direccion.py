# Generated by Django 3.2.6 on 2021-09-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odontologia', '0006_alter_paciente_obra_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obrasocial',
            name='direccion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]