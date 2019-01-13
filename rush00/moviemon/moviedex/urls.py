from django.urls import path, include
from moviedex.views import MovieDex


urlpatterns = [
    path('', MovieDex.as_view()),
    path('<str:id>/', include('detail.urls')),
]
