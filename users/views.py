from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from users.forms import UsersRegisterForm, UsersProfileForm
from users.models import ServiceClient


class UsersCreateView(CreateView):
    model = ServiceClient
    form_class = UsersRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зар5егистрировались на проекте',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)

class UsersUpdateView(UpdateView):
    model = ServiceClient
    form_class = UsersProfileForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

class UsersDeleteView(DeleteView):
    model = ServiceClient
    success_url = reverse_lazy('mailing:mailing_list')

class VerificationView(DeleteView):
    model = ServiceClient
    success_url = reverse_lazy('mailing:mailing_list')

