from django.shortcuts import render
from django.urls import reverse_lazy

from django_registration.backends.activation.views import RegistrationView, ActivationView
from django_registration.forms import RegistrationFormUniqueEmail

from sh_blog.models import UserProfile
# Create your views here.
class MyRegistrationView(RegistrationView):
    form_class = RegistrationFormUniqueEmail
    disallowed_url = reverse_lazy("accounts:django_registraion_disallowed")
    success_url = reverse_lazy("accounts:django_registration_complete")            


class MyActivationView(ActivationView):
    success_url = reverse_lazy("accounts:django_registration_activation_complete")

    def activate(self, *args, **kwargs):
        user = super().activate(*args, **kwargs)
        self.new_profile(user)
        return user


    def new_profile(self, user):
        new_profile = UserProfile()
        new_profile.user = user
        new_profile.save()