from django.db import models
from django.utils import timezone


class Mailing(models.Model):
    PERIOD_CHOICES = (
        (1, 'Раз в день'),
        (7, 'Раз в неделю'),
        (30, 'Раз в месяц'),
    )
    STATUS_CHOICES = (
        ('completed', 'Завершена'),
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('failed', 'Ошибка'),
    )

    mailing_time = models.DateTimeField(
        verbose_name='Время рассылки',
        default=timezone.now(),
        help_text='Укажите время для отправки рассылки в формате: хх.хх.хххх хх:хх:хх'
    )
    periodicity = models.IntegerField(
        verbose_name='Периодичность',
        choices=PERIOD_CHOICES,
        default=1
    )
    mailing_status = models.CharField(verbose_name='Статус рассылки',
                                      max_length=20,
                                      choices=STATUS_CHOICES,
                                      default='created'
                                      )

    def __str__(self):
        return f'{self.mailing_time} - {self.mailing_status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MessageSend(models.Model):
    letter_subject = models.CharField(max_length=150, verbose_name='тема письма')
    letter_body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.letter_subject} - {self.letter_body}'

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'
