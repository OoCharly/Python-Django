from django.urls import path
from titlescreen.views import TitleScreen

urlpatterns = [
    path('', TitleScreen.as_view()),
]
