from django.urls import path
from worldmap.views import WorldMap

urlpatterns = [
    path('', WorldMap.as_view()),
]
