from django.shortcuts import HttpResponse, render
from django.views import View
import psycopg2


class Ex06(View):

    def db_connect(self):
        co = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret',
        )
        return co

    def init(self):
        try:
            co = self.db_connect()
            co.cursor().execute(
                "CREATE TABLE IF NOT EXISTS ex06_movies ("
                "title varchar(64) UNIQUE NOT NULL,"
                "episode_nb  integer PRIMARY KEY,"
                "opening_crawl text,"
                "director varchar(32) NOT NULL,"
                "producer varchar(128) NOT NULL,"
                "release_date date NOT NULL,"
                "created timestamp DEFAULT(now()),"
			    "updated timestamp DEFAULT(now())"
                ")"
            )
            co.commit()

            co.cursor().execute(
                "CREATE OR REPLACE FUNCTION update_changetimestamp_column() "
                "RETURNS TRIGGER AS $$ "
                "BEGIN "
                "NEW.updated = now();"
                "NEW.created = OLD.created;"
                "RETURN NEW;"
                "END;"
                "$$ language 'plpgsql';"
                "CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE "
                "ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE "
                "update_changetimestamp_column();"
            )
            co.commit()

            co.close()
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)

    def populate(self):
        try:
            co = self.db_connect()
            curr = co.cursor()

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
                        " INSERT INTO ex06_movies("
                        "episode_nb, title, director, producer, release_date) VALUES (%s,%s,%s,%s,%s)",
                        (item[0], item[1], item[2], item[3], item[4]))
                    co.commit()
                    mess.append(item[1] + " => OK<br>")
                except Exception as e:
                    mess.append(item[1] + ": " + e.args[0] + "<br>")
            co.close()

            return HttpResponse(mess)
        except Exception as e:
            return HttpResponse(e)

    def display(self, request):
        try:
            co = self.db_connect()
            cursor = co.cursor()

            cursor.execute("SELECT * FROM ex06_movies ORDER BY episode_nb")
            data = cursor.fetchall()
            list = []
            for row in data:
                list.append(row)
            if not list:
                co.close()
                raise Exception
            co.close()
            return render(request, 'ex02/display.html', {'films': list})
        except Exception as e:
            return HttpResponse("No data available")

    def update(self, request):
        try:
            co = self.db_connect()
            cursor = co.cursor()

            if request.method == 'POST':
                form = request.POST
                cursor.execute(
                    "UPDATE ex06_movies SET opening_crawl = %s WHERE episode_nb = %s",
                    (form['crawl_text'], form['title'])
                )
                co.commit()

            cursor.execute("SELECT episode_nb, title FROM ex06_movies ORDER BY episode_nb")
            data = cursor.fetchall()
            list = []
            for row in data:
                list.append(row)
            if not list:
                co.close()
                raise Exception("No data available")
            co.close()
        except Exception as e:
            return HttpResponse(e)
        return render(request, 'ex06/update.html', {'films': data})

    def get(self, request, action=None):
        if action == 'init':
            return self.init()
        elif action == 'populate':
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

# Create your views here.
