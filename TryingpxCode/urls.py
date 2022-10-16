from django.urls import path
from TryingpxCode.views import indexpxcode

app_name = 'TryingpxCode'

urlpatterns = [
    path('', indexpxcode, name='indexpxcode'),
]