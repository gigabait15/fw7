from django.urls import path
from mailinglog.views import MailingLogsListView, MailingLogsDetailView
from users.apps import UsersConfig


app_name = UsersConfig.name


urlpatterns = [
    path('list_mailinglogs/', MailingLogsListView.as_view(), name='mailinglogs'),
    path('detail_mailinglogs/<int:pk>/', MailingLogsDetailView.as_view(), name='detail_mailinglogs'),
]