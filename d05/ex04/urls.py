from django.urls import path
from ex04.views import Ex04

from . import views

urlpatterns = [
    path('<str:action>/', Ex04.as_view()),
]
