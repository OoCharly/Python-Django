from django.urls import path
from ex00.views import Ex00

from . import views

urlpatterns = [
    path('init/', Ex00.as_view()),
]
