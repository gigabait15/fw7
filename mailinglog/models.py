from django.db import models
from mailing.models import Mailing


class MailingLogs(models.Model):
    datatime_last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки')
    attempt_status = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='статус попытки')
    mail_server_response = models.CharField(max_length=100, verbose_name='ответ почтового сервера, если он был')

    def __str__(self):
        return f'{self.datatime_last_attempt} - {self.attempt_status}'

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'

