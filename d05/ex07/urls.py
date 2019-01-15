from django.urls import path
from ex07.views import Ex07

from . import views

urlpatterns = [
    path('<str:action>/', Ex07.as_view()),
]
