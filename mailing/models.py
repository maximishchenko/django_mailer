from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class List(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Дата редактирования')
    title = models.CharField(max_length=200, verbose_name = 'Заголовок рассылки')
    subject = models.CharField(max_length=200, verbose_name = 'Тема сообщения')
    text = RichTextUploadingField(verbose_name = 'Текст сообщеняи')
    attachments = models.FileField(upload_to='mailing_attachments', verbose_name = 'Вложения', blank=True)
    status = models.BooleanField(default=False, verbose_name = 'Статус')
    author = models.CharField(max_length=200, verbose_name = 'Автор', blank=True)

    def publish(self):
        self.save()

    class Meta:
        db_table = 'mailing_list'
        verbose_name = u'Список рассылок'
        verbose_name_plural = u'Списки рассылок'

    def __str__(self):
        return self.title