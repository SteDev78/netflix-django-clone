from core.views import Home
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('',Home.as_view()),
]
