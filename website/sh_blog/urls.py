from django.urls import path
from .views import index
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sh_blog'

urlpatterns = [
    path('', index, name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)