from django import forms
from mailinglog.models import MailingLogs
from users.forms import StyleFormMixin


class MailingLogsForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailingLogs
        fields = '__all__'