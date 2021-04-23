from django.urls import path
from .views import *
from MySite import settings
urlpatterns = [
    path('', index),
    path('test/', test)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)