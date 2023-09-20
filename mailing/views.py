from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from mailing.forms import MailingForm, MessageSendForm
from mailing.models import Mailing, MessageSend


# Контроллеры модели Mailing

class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'

class MailingDetailView(DetailView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_detail.html'

class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing')
    template_name = 'mailing/mailing_form.html'

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing')
    template_name = 'mailing/mailing_form.html'

class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing')
    template_name = 'mailing/mailing_confirm_delete.html'


# Контроллер модели MessageSend
class MessageSendListView(ListView):
    model = MessageSend
    template_name = 'mailing/message_list.html'

class MessageSendDetailView(DetailView):
    model = MessageSend
    form_class = MessageSendForm
    template_name = 'mailing/message_detail.html'

class MessageSendCreateView(CreateView):
    model = MessageSend
    form_class = MessageSendForm
    success_url = reverse_lazy('mailing')
    template_name = 'mailing/message_form.html'

class MessageSendUpdateView(UpdateView):
    model = MessageSend
    form_class = MessageSendForm
    success_url = reverse_lazy('mailing')
    template_name = 'mailing/message_form.html'

class MessageSendDeleteView(DeleteView):
    model = MessageSend
    form_class = MessageSendForm
    success_url = reverse_lazy('mailing')
    template_name = 'mailing/message_confirm_delete.html'

def send_mailings():
    current_time = now()

    mailing_items = Mailing.objects.all()
    message = MessageSend.objects.all()

    for mailing_item in mailing_items:
        if mailing_item.objects(
            mailing_time=current_time,
            periodicity=1,
            mailing_status='created',
        ):
            subject = message.letter_subject
            message_body = message.letter_body

            send_mail(subject, message_body, os.getenv('EMAIL_HOST_USER'), [os.getenv('EMAIL_HOST_USER')])

            mailing.mailing_status = 'completed'
            mailing.save()

        elif mailing_item.objects(
            mailing_time=current_time,
            periodicity=7,
            mailing_status='created',
        ):
            subject = message.letter_subject
            message_body = message.letter_body

            send_mail(subject, message_body, os.getenv('EMAIL_HOST_USER'), [os.getenv('EMAIL_HOST_USER')])

            mailing.mailing_status = 'completed'
            mailing.save()

        elif mailing_item.objects(
                mailing_time=current_time,
                periodicity=30,
                mailing_status='created',
        ):
            subject = message.letter_subject
            message_body = message.letter_body

            send_mail(subject, message_body, os.getenv('EMAIL_HOST_USER'), [os.getenv('EMAIL_HOST_USER')])

            mailing.mailing_status = 'completed'
            mailing.save()

