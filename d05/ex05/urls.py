from django.urls import path
from ex05.views import Ex05

from . import views

urlpatterns = [
    path('<str:action>/', Ex05.as_view()),
]
