from django.urls import path

from . import index

app_name = 'pika_app'
urlpatterns = [
    path('', index.IndexView.as_view(), name='index'),
]
