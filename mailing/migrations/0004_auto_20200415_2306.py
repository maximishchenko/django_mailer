# Generated by Django 3.0.5 on 2020-04-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_auto_20200415_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
        migrations.AlterModelTable(
            name='list',
            table='mailing_list',
        ),
    ]
