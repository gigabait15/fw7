from django.contrib import admin
from mailing.models import Mailing, MessageSend


@admin.register(Mailing)
class Mailing(admin.ModelAdmin):
    list_display = ('mailing_time', 'periodicity', 'mailing_status')
    list_filter = ('mailing_status',)
    search_fields = ('periodicity', 'mailing_time',)


@admin.register(MessageSend)
class MessageSend(admin.ModelAdmin):
    list_display = ('letter_subject', 'letter_body')
    list_filter = ('letter_subject',)
    search_fields = ('letter_subject',)
