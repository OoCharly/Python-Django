from django.shortcuts import render
from django.views import View
from moviemon.data import Data




class Detail(View):
    data=Data()

    def get(self, request, id):
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
        
        
        return render(request, 'detail/index.html', context)