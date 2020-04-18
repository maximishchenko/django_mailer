# Generated by Django 2.2.12 on 2020-04-15 19:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_auto_20200415_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'verbose_name': 'Список рассылок', 'verbose_name_plural': 'Списки рассылок'},
        ),
        migrations.AddField(
            model_name='list',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='list',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='Тема сообщения'),
        ),
        migrations.AlterField(
            model_name='list',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст сообщеняи'),
        ),
    ]