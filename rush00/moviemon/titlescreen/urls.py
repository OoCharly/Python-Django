from django.urls import path
from titlescreen.views import TitleScreen

from . import views

urlpatterns = [
    path('', TitleScreen.as_view()),
]
