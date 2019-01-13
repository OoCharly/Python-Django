from django.urls import path
from battle.views import Battle

urlpatterns = [
    path('<str:id>/', Battle.as_view()),
]
