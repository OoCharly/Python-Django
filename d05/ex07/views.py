from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Movies


class Ex07(View):

    def populate(self):
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
            try:
                Movies(
                    episode_nb=item[0],
                    title=item[1],
                    director=item[2],
                    producer=item[3],
                    release_date=item[4],
                ).save()
                mess.append(item[1] + " => OK<br>")
            except Exception as e:
                mess.append(item[1] + " => Fail " + str(e) + " <br>")
        return HttpResponse(mess)

    def display(self, request):
        try:
            out = []
            for row in Movies.objects.all():
                out.append((row.episode_nb, row.title, row.opening_crawl,row.director, row.producer, row.release_date))
            if not out:
                raise Exception
            return render(request, 'ex02/display.html', {'films': out})
        except Exception as e:
            return HttpResponse("No data available")

    def update(self, request):
        if request.method == 'POST':
            form = request.POST
            try:
                instance = Movies.objects.get(episode_nb=int(form['title']))
                instance.opening_crawl = form['crawl_text']
                instance.save()
            except Exception as e:
                return HttpResponse(e, status=500)
        out = []
        data = Movies.objects.values_list('episode_nb', 'title')
        for row in data:
            out.append((row[0], row[1]))
        if not out:
            return HttpResponse("No data available")
        return render(request, 'ex06/update.html', {'films': out})

    def get(self, request, action=None):
        if action == 'populate':
            return self.populate()
        elif action == 'display':
            return self.display(request)
        elif action == 'update':
            return self.update(request)
        else:
            return HttpResponse("404 - Not Found", status=404)

    def post(self, request, action=None):
        if action == 'update':
            return self.update(request)
        else:
            return HttpResponse("404 - Not Found", status=404)
# Create your views here.

# Create your views here.
