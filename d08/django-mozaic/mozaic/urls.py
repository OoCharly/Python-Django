from django.urls import path
from .views import Mozaic

urlpatterns = [
    path(r'', Mozaic.as_view()),
]
