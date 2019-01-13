from django.shortcuts import render
from django.views import View
from moviemon.data import Data
import random
from django.shortcuts import redirect


class WorldMap(View):
    data = Data()

    def get(self, request):
        req = request.GET
        event = {}

        controls = {
            'up':'?move=up', 
            'right':'?move=right',
            'down':'?move=down',
            'left':'?move=left',
            'A':'',
            'B':'',
            'start':'/options',
            'select':'/moviedex',
        }

        if random.randrange(101) > 80 and req.get('c', 'False') == 'False':
            event.update({'moviemon': self.data.get_random_movie()})
            controls['A'] = '/battle/' + event['moviemon']
        if 'moviemon' not in event and req.get('c', False) == 'False':
            balls = random.randrange(1,3)
            self.data.increase_balls(balls)
            event.update({'balls': str(balls)})

        if 'move' in req:
            c = self.data.move(req['move'])
            return redirect('/worldmap?c=' + str(c)) #pour eviter le move lors de refresh TODO
        if 'new' in req:
            self.data.clean_data_for_new_game()
            return redirect('/worldmap') #pour eviter le move lors de refresh TODO


        context = self.data.dump()
        
        context.update({'event': event})
        context.update({'size': (range(context['size'][0]), range(context['size'][0]))})
        context.update({'controls':controls})
        return render(request, 'worldmap/index.html', context)

