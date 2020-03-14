from django.urls import path
from .views import index, post_detail, not_about_work
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sh_blog'

urlpatterns = [
    path('', index, name='main'),
    path('not-work/', not_about_work, name='not_work'),
    path('<slug:slug>/', post_detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)