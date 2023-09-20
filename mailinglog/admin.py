from django.contrib import admin
from mailinglog.models import MailingLogs


@admin.register(MailingLogs)
class MailingLogs(admin.ModelAdmin):
    list_display = ('datatime_last_attempt', 'attempt_status', 'mail_server_response')
    list_filter = ('datatime_last_attempt',)
    search_fields = ('attempt_status',)
