# Generated by Django 3.0.1 on 2020-05-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas', '0005_auto_20200515_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('Currency_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('Currency_name', models.CharField(max_length=30, verbose_name='Währungsname')),
                ('Currency_symbol', models.CharField(max_length=10, verbose_name='Währungssymbol')),
            ],
        ),
    ]