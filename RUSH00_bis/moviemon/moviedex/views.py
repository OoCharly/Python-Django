from django.shortcuts import render
from django.views import View
from moviemon.data import Data



class MovieDex(View):
    data = Data()

    def get(self, request):
        context = self.data.dump()
        req = request.GET
        select = 1
        if req:
            if req.get('move', False):
                if req['move'] == 'up':
                    if int(req['s']) > 1:
                        select = int(req['s']) - 1
                    else:
                        select = len(context['capture_movies'])
                elif req['move'] == 'down':
                    if int(req['s']) < len(context['capture_movies']):
                        select = int(req['s']) + 1
                    else:
                        select = 1

        context.update({'select': select})
        context.update({'columns': str(int(len(context['capture_movies'] / 3)))})

    
        a = ''
        if (len(context['capture_movies']) > 0):
            a = context['capture_movies'][context['select'] - 1]

        controls = {
        'up':'?move=up&s=' + str(context['select']),
        'right':'?move=down&s=' + str(context['select']),
        'down':'?move=down&s=' + str(context['select']),
        'left':'?move=up&s=' + str(context['select']),
        'A':'/moviedex/' + a,
        'B':'',
        'start':'',
        'select':'/worldmap',
        }

        context.update({'controls':controls})

        return render(request, 'moviedex/index.html', context)

# Create your views here.
