from django.urls import path
from .views import index

app_name = 'sh_blog'

urlpatterns = [
    path('', index, name='main'),
]
