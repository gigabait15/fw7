from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class ServiceClient(User):
    email_client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='email',
                                         related_name='client_emails')
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    service_client_is_active = models.BooleanField(default=False, verbose_name='активирован')

    def __str__(self):
        return f'{self.full_name} - {self.email}'

    class Meta:
        verbose_name = 'Cервис клиент'
        verbose_name_plural = 'Cервис клиенты'
