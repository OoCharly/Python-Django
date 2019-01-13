from django.shortcuts import render
from django.views import View
from moviemon.data import Data
from django.http import Http404 



class Detail(View):
    data=Data()

    def get(self, request, id):
        context = self.data.dump()
        try:
            req = request.GET
            controls = {
                'up':'', 
                'right':'',
                'down':'',
                'left':'',
                'A':'',
                'B':'/moviedex',
                'start':'',
                'select':''
            }
            context={}
            context.update({'controls': controls})
            context.update({'movie': self.data.get_movie(id)})
        except:
            raise Http404('Sorry the film #{} was not found'.format(id))
        return render(request, 'detail/index.html', context)