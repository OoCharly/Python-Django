from django.shortcuts import render
from django.views import View
from moviemon.data import Data
import random

class Battle(View):
    data=Data()

    def _throw_result(self, strengh, rating):
        prob = 50 - (rating * 10) + (strengh * 5)
        if prob < 1:
            prob = 1
        elif prob > 90:
            prob = 90
        return prob

    def get(self, request, id):
        req = request.GET

        controls = {
            'up':'', 
            'right':'',
            'down':'',
            'left':'',
            'A':'?move=throw',
            'B':'/worldmap',
            'start':'',
            'select':'',
        }

        context = self.data.dump()
        context.update({'movie': self.data.get_movie(id)})

        proba = self._throw_result(len(context['capture_movies']), float(context['movie']['imdbRating']))
        context.update({'proba':proba})

        if req:
            if req['move'] and req['move'] == 'throw':
                if context['balls'] > 0:
                    self.data.decrease_balls()
                    
                    if random.randrange(101) <= proba:
                        self.data.capture_movie(id)
                        controls.update({'A':''})
                        context.update({'event': 'You Did It !! '})
                    else:
                        context.update({'event': 'Looser !! '})
                else:
                    context.update({'event': 'Stop throw pebbles to this poor Moviemon'})

        context.update({'controls': controls})        
        return render(request, 'battle/index.html', context)
# Create your views here.
