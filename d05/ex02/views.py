from django.shortcuts import HttpResponse, render
from django.views import View
import psycopg2


class Ex02(View):
    co = psycopg2.connect(
        database='formationdjango',
        host='localhost',
        user='djangouser',
        password='secret',
    )

    def init(self):
        try:
            self.co.cursor().execute(
                "CREATE TABLE IF NOT EXISTS ex02_movies ("
                "title varchar(64) UNIQUE NOT NULL,"
                "episode_nb  integer PRIMARY KEY,"
                "opening_crawl text,"
                "director varchar(32) NOT NULL,"
                "producer varchar(128) NOT NULL,"
                "release_date date NOT NULL"
                ")"
            )
            self.co.commit()
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)

    def populate(self):
        try:
            curr = self.co.cursor()

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
                    curr.execute(
                        " INSERT INTO ex02_movies("
                        "episode_nb, title, director, producer, release_date) VALUES (%s,%s,%s,%s,%s)",
                        (item[0], item[1], item[2], item[3], item[4]))
                    self.co.commit()
                    mess.append(item[1] + " => OK<br>")
                except Exception as e:
                    mess.append(item[1] + ": " + e.args[0] + "<br>")
                    self.co.commit()

            return HttpResponse(mess)
        except Exception as e:
            return HttpResponse(e)

    def display(self, request):
        try:
            cursor = self.co.cursor()

            cursor.execute("SELECT * FROM ex02_movies")
            data = cursor.fetchall()
            list = []
            for row in data:
                list.append(row)
            if not list:
                raise Exception
            return render(request, 'ex02/display.html', {'films': list})
        except Exception as e:
            return HttpResponse("No data available")

    def get(self, request, action=None):
        if action == 'init':
            return self.init()
        elif action == 'populate':
            return self.populate()
        elif action == 'display':
            return self.display(request)
        else:
            return HttpResponse("404 - Not Found", status=404)
# Create your views here.
