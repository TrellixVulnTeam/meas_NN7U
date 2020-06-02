# Generated by Django 3.0.1 on 2020-05-15 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meas', '0002_auto_20200404_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('Unit_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_symbol', models.CharField(max_length=5, verbose_name='Einheitssymbol')),
                ('Unit_name', models.CharField(max_length=50, verbose_name='Einheitsname')),
                ('Unit_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Einheitsbeschreibung')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product_ppu_net',
        ),
        migrations.AddField(
            model_name='product',
            name='Product_pppu_net',
            field=models.FloatField(default=0, verbose_name='Einkaufspreis pro Einheit (netto)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_sppu_net',
            field=models.FloatField(default=0, verbose_name='Verkaufspreis pro Einheit (netto)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meas.Unit'),
        ),
    ]