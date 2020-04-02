from django.urls import path, include
from .views import MyRegistrationView, MyActivationView
from django.views.generic.base import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path(
       "accounts/activate/complete/",
       TemplateView.as_view(
           template_name="django_registration/activation_complete.html"
       ),
       name="django_registration_activation_complete",
    ),
    path(
        "accounts/activate/<str:activation_key>/",
        MyActivationView.as_view(),
        name="django_registration_activate",
    ),
    path(
        "accounts/register/",
        MyRegistrationView.as_view(),
        name="django_registration_register",
    ),
    path(
        "accounts/register/complete/",
        TemplateView.as_view(
            template_name="django_registration/registration_complete.html"
        ),
        name="django_registration_complete",
    ),
    path(
        "accounts/register/closed/",
        TemplateView.as_view(
            template_name="django_registration/registration_closed.html"
        ),
        name="django_registration_disallowed",
    ),
]