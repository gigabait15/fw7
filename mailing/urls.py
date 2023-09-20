from django.urls import path
from mailing.views import MessageSendListView, MessageSendDetailView, MessageSendCreateView, MessageSendUpdateView, \
    MessageSendDeleteView, MailingListView, MailingDetailView, MailingCreateView, MailingDeleteView
from users.apps import UsersConfig


app_name = UsersConfig.name


urlpatterns = [
    path('', MailingListView.as_view(), name='mailing'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('list_message/', MessageSendListView.as_view(), name='list_message'),
    path('create_message/', MessageSendDetailView.as_view(), name='create_message'),
    path('view_message/<int:pk>/', MessageSendCreateView.as_view(), name='view_message'),
    path('edit_message/<int:pk>/', MessageSendUpdateView.as_view(), name='edit_message'),
    path('delete_message/<int:pk>/', MessageSendDeleteView.as_view(), name='delete_message'),
]