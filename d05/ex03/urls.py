from django.urls import path
from ex03.views import Ex03

from . import views

urlpatterns = [
    path('<str:action>/', Ex03.as_view()),
]
