from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Movies


class Ex03(View):

    def populate(self):
        try:
            l = [
                (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
                (2, 'Attack of the Clones', 'Georges Lucas', 'Rick McCallum', '2002-05-16'),
                (3, 'Revenge of the Sith', 'Georges Lucas', 'Rick McCallum', '2005-05-19'),
                (4, 'A New Hope', 'Georges Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
                (5, 'The Empire Strike Backs', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
                (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, Georges Lucas, Rick McCallum',
                 '1983-05-25'),
                (7, 'The Force Awakens', 'J.J. Abrams', 'Kathleen Kennedy, J.J. Abrams, Bryan Burk', '2015-02-11')
            ]

            mess = []
            for item in l:
                Movies(
                    episode_nb=item[0],
                    title=item[1],
                    director=item[2],
                    producer=item[3],
                    release_date=item[4],
                ).save()
                mess.append(item[1] + " => OK<br>")
            return HttpResponse(mess)
        except Exception as e:
            return HttpResponse(e, status=500)

    def display(self, request):
        try:
            out = []
            for row in Movies.objects.all():
                out.append((row.episode_nb, row.title, row.opening_crawl,row.director, row.producer, row.release_date))
                print(out)
            if not out:
                raise Exception
            return render(request, 'ex02/display.html', {'films': out})
        except Exception as e:
            return HttpResponse("No data available")

    def get(self, request, action=None):
        if action == 'populate':
            return self.populate()
        elif action == 'display':
            return self.display(request)
        else:
            return HttpResponse("404 - Not Found", status=404)
