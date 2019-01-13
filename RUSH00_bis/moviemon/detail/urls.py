from django.urls import path
from battle.views import Battle
from detail.views import Detail

urlpatterns = [
    path('', Detail.as_view()),
]