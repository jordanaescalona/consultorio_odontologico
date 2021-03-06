# Generated by Django 3.2.6 on 2021-09-25 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('odontologia', '0002_auto_20210914_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='hc',
            field=models.IntegerField(blank=True, null=True, verbose_name='N° historia clínica'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numOS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paciente_obraSocial', to='odontologia.obrasocial', verbose_name='Obra Social'),
        ),
    ]
