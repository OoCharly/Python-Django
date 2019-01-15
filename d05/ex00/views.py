from django.shortcuts import HttpResponse
from django.views import View
import psycopg2



class Ex00(View):

    def get(self, request):
        try:
            co = psycopg2.connect(
                database='formationdjango',
                host='localhost',
                user='djangouser',
                password='secret',
            )

            co.cursor().execute(
                "CREATE TABLE IF NOT EXISTS ex00_movies ("
                "title varchar(64) UNIQUE NOT NULL,"
                "episode_nb  integer PRIMARY KEY,"
                "opening_crawl text,"
                "director varchar(32) NOT NULL,"
                "producer varchar(128) NOT NULL,"
                "release_date date NOT NULL"
                ")"
            )
            co.commit()
            co.close()
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)

# Create your views here.
