from django.shortcuts import render
from django.views import View
from moviemon.data import Data


class Options(View):

    def get(self, request):
        controls = {
            'up':'', 
            'right':'',
            'down':'',
            'left':'',
            'A':'save_game',
            'B':'/',
            'start':'/worldmap',
            'select':'',
            }

        context = {}
        context.update({'controls':controls})

        return render(request, 'options/index.html', context)


class SaveGame(View):
    data = Data()

    def slots_str(self):
        slots = Data.get_slots()
        iter = ['a', 'b', 'c']
        slots_str = []
        for i in iter:
            if slots[i][1] != 0:
                slots_str.append(str(slots[i][0]+'/'+slots[i][1]))
            else:
                slots_str.append("Free")
        return (slots_str)

    def get(self, request):
        context = self.data.dump()
        iter = ['a', 'b', 'c']
        context.update({'slots': self.slots_str()})
        req = request.GET
        select = 0
        if req:
            select = int(req.get('s', 0))
            if req.get('save', True) == 'True' and int(req.get('s', 0)) in range(3):
                self.data.hard_save(iter[int(req.get('s', 0))])
                context.update({'slots': self.slots_str()})
            elif req.get('move', True):
                if req['move'] == 'up':
                    if int(req['s']) > 0:
                        select = select - 1
                    else:
                        select = 2
                elif req['move'] == 'down':
                    if select < 2:
                        select = select + 1
                    else:
                        select = 0

        context.update({'select': select})

        controls = {
            'up':'?save=False&move=up&s=' + str(select), 
            'right':'',
            'down':'?save=False&move=down&s=' + str(select),
            'left':'',
            'A':'?save=True&s=' + str(select),
            'B':'/options',
            'start':'',
            'select':'',
        }
        context.update({'controls':controls})
        
        return render(request, 'options/save_game.html', context)


class LoadGame(View):
    data = Data()

    def slots_str(self):
        slots = Data.get_slots()
        iter = ['a', 'b', 'c']
        slots_str = []
        for i in iter:
            if slots[i][1] != 0:
                slots_str.append(str(slots[i][0]+'/'+slots[i][1]))
            else:
                slots_str.append("Free")
        return (slots_str)

    def get(self, request):
        context = self.data.dump()
        slots = Data.get_slots()
        print("slots" + str(slots))
        iter = ['a', 'b', 'c']
        load = False

        context.update({'slots': self.slots_str()})
        req = request.GET
        select = 0
        if req:
            select = int(req.get('s', 0))
            if req.get('load', True) == 'True' and select in range(3):
                slots = Data.get_slots()
                slot = slots[iter[select]]
                if slot[1] != 0:

                    slot = str(iter[select])
                    print("open slot : " + slot )
                    print("HERE ")
                    self.data.load(slot)
                    load = True
            elif req.get('move', True):
                if req['move'] == 'up':
                    if int(req['s']) > 0:
                        select = select - 1
                    else:
                        select = 2
                elif req['move'] == 'down':
                    if select < 2:
                        select = select + 1
                    else:
                        select = 0

        
        context.update({'select': select})
        

        if load == False:
            a = '?load=True&s=' + str(select)
        else:
            a = '/worldmap'

        controls = {
            'up':'?load=False&move=up&s=' + str(select), 
            'right':'',
            'down':'?load=False&move=down&s=' + str(select),
            'left':'',
            'A':a,
            'B':'/',
            'start':'',
            'select':'',
        }

        context.update({'controls':controls})

        return render(request, 'options/load_game.html', context)
# Create your views here.
