from django.shortcuts import render
from django.views.generic import ListView, DetailView
from mailinglog.forms import MailingLogsForm
from mailinglog.models import MailingLogs


class MailingLogsListView(ListView):
    model = MailingLogs

class MailingLogsDetailView(DetailView):
    model = MailingLogs
    form_class = MailingLogsForm
