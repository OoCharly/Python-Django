from django.urls import path
from ex02.views import Ex02

from . import views

urlpatterns = [
    path('<str:action>/', Ex02.as_view()),
]
