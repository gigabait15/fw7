from django import forms
from mailing.models import Mailing, MessageSend
from users.forms import StyleFormMixin


class MailingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSendForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MessageSend
        fields = '__all__'