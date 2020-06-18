# Generated by Django 3.0.1 on 2020-06-14 16:23

from django.db import migrations, models
import meas.models


class Migration(migrations.Migration):

    dependencies = [
        ('meas', '0014_auto_20200614_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_project',
            name='CP_number',
        ),
        migrations.AddField(
            model_name='customer_project',
            name='CP_name',
            field=models.CharField(default='TesT', max_length=50, verbose_name='Bauvorhaben'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='Order_number',
            field=models.CharField(default=meas.models.create_order_number, max_length=200, verbose_name='Auftragsnummer'),
        ),
    ]
