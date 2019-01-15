from django.urls import path
from ex06.views import Ex06

from . import views

urlpatterns = [
    path('<str:action>/', Ex06.as_view()),
]
