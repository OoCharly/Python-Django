from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class TitleScreen(View):

    def get (self, request):

        controls = {
        'up':'', 
        'right':'',
        'down':'',
        'left':'',
        'A':'/worldmap?new=""',
        'B':'/options/load_game',
        'start':'',
        'select':'',
        }
        context = {}
        context.update({'controls':controls})
        return render(request, 'titlescreen/index.html', context)
