from django.urls import path
from options.views import Options, SaveGame, LoadGame

urlpatterns = [
    path('', Options.as_view()),
    path('save_game/', SaveGame.as_view()),
    path('load_game/', LoadGame.as_view()),
]
