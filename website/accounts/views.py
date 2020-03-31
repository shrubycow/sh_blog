from django.shortcuts import render
from django.urls import reverse_lazy

from django_registration.backends.activation.views import RegistrationView, ActivationView
# Create your views here.
class MyRegistrationView(RegistrationView):
    disallowed_url = reverse_lazy("accounts:django_registraion_disallowed")
    success_url = reverse_lazy("accounts:django_registration_complete")


class MyActivationView(ActivationView):
    success_url = reverse_lazy("accounts:django_registration_activation_complete")