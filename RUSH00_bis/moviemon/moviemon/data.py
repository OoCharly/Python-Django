import pickle
import random
from django.conf import settings
from django.http import Http404
#import settings
import requests
import os, glob, re


def parse(json):
    need = [
        'Title',
        'Year',
        'Director',
        'Actors',
        'Plot',
        'Poster',
        'imdbRating',
    ]
    out = {}
    for obj in need:
        out.update({obj: json.get(obj)})
    return out


def request_movie_info():
    url = "http://www.omdbapi.com/"
    out = {}
    ids = settings.MOVIEMON_SETTINGS['MOVIES_ID']
    for id in ids:
        payload = {
            'apikey': '7c3438b1',
            'i': id,
        }
        response = requests.get(url, payload)
        out.update({id: parse(response.json())})
    return out



def request_movie_info_debug():
    return {'tt0111161':{
                "Title": "The Shawshank Redemption",
                "Year": "1994",
                "Director": "Frank Darabont",
                "Actors": "Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler",
                "Plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                "Poster": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
                "imdbRating": "9.3",
            },
            'tt0068646':{
                "Title":"The Godfather",
                "Year":"1972",
                "Director":"Francis Ford Coppola",
                "Actors":"Marlon Brando, Al Pacino, James Caan, Richard S. Castellano",
                "Plot":"The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                "Poster":"https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
                "imdbRating":"9.2",
            },
            'tt0079788':{
               "Title":"Zombie Holocaust",
                "Year":"1980",
                "Director":"Marino Girolami)",
                "Actors":"Ian McCulloch, Alexandra Delli Colli, Sherry Buchanan, Peter O'Neal",
                "Plot":"An expedition in the East Indies, encounters not only the cannibals they were looking for, but also an evil scientist and his zombie army.",
                "Poster":"https://m.media-amazon.com/images/M/MV5BYTc1YzgxNzktMWY4Mi00ZmUwLTkwODktMzAwZDUwMzA0YTRhXkEyXkFqcGdeQXVyMzMwMjI2NA@@._V1_SX300.jpg",
                "imdbRating":"5.3",
           },
            'tt0804492':{
                "Title":"The Hottie & the Nottie",
                "Year":"2008",
                "Director":"Tom Putnam",
                "Plot":"A woman agrees to go on a date with a man only if he finds a suitor for her unattractive best friend.",
                "Poster":"https://ia.media-imdb.com/images/M/MV5BMTA2NDc1ODUxNDZeQTJeQWpwZ15BbWU3MDQ1MjM1NTE@._V1_SX300.jpg",
                "imdbRating":"1.9",
                "Actors":"Paris Hilton, Joel David Moore, Christine Lakin, Johann Urb",
            }
        }

class Data():
    _capture_movies = []
    if (settings.DEBUG == False):
        _x = int(settings.MOVIEMON_SETTINGS['SIZE'][0] / 2)
        _y = int(settings.MOVIEMON_SETTINGS['SIZE'][1] / 2)
        _movies = request_movie_info()
        _free_movies = settings.MOVIEMON_SETTINGS['MOVIES_ID']
        _balls = int(settings.MOVIEMON_SETTINGS['BALLS'])
    else:
        _x = int(settings.MOVIEMON_SETTINGS_DEBUG['SIZE'][0] / 2)
        _y = int(settings.MOVIEMON_SETTINGS_DEBUG['SIZE'][1] / 2)
        _movies = request_movie_info_debug()
        _free_movies = settings.MOVIEMON_SETTINGS_DEBUG['MOVIES_ID']
        _balls = int(settings.MOVIEMON_SETTINGS_DEBUG['BALLS'])

    

    def __init__(self):
        pass

    def save_state(self):
        self.hard_save('run.txt')

    def hard_save(self, slot):
        # slot = slot_A.txt | slot_B.txt | slot_B.txt |
        files = glob.glob('saved_game/slot' + slot + "_*_*.mmg" )
        if len(files) > 0:
            os.remove(files[0])
        file_name = "saved_game/slot" + slot + "_" + str(len(Data._capture_movies)) + "_" + str(len(Data._movies)) + ".mmg"
        self._x = Data._x
        self._y = Data._y
        self._movies = Data._movies
        self._free_movies = Data._free_movies
        self._capture_movies = Data._capture_movies
        self._balls = Data._balls

        pickle.dump(self, open(file_name, 'wb'))

    def clean_data_for_new_game(self):
        Data._strengh = 10
        Data._x = int(settings.MOVIEMON_SETTINGS['SIZE'][0] / 2)
        Data._y = int(settings.MOVIEMON_SETTINGS['SIZE'][1] / 2)
        Data._movies = request_movie_info()
        Data._free_movies = settings.MOVIEMON_SETTINGS['MOVIES_ID']
        Data._capture_movies = []
        Data._balls = int(settings.MOVIEMON_SETTINGS['BALLS'])

    def load(self, slot):
        #run.txt | slot_A.txt | slot_B.txt | slot_B.txt |
        files = glob.glob("saved_game/slot" + slot + "_*_*.mmg" )
        try:
            if (files[0]):
                obj_data = pickle.load(open(files[0], 'rb'))
            
                Data._x = obj_data._x
                Data._y = obj_data._y
                Data._movies = obj_data._movies
                Data._free_movies = obj_data._free_movies
                Data._capture_movies = obj_data._capture_movies
                Data._balls = obj_data._balls
            else:
                raise Exception("Save File for slot %s Does not Exist".format(slot))
        except Exception as e:
            print(e)


    def dump(self):
        state = {
            'size' : settings.MOVIEMON_SETTINGS['SIZE'],
            'pos_x' : int(Data._x),
            'pos_y': int(Data._y),
            'movies' : Data._movies,
            'free_movies' : Data._free_movies,
            'capture_movies' : Data._capture_movies,
            'encounter': False,
            'balls': Data._balls,
        }
        return(state)
        
    def get_random_movie(self):
        if len(Data._free_movies) != 0 :
            nb_movies = len(Data._free_movies)
            nb_movies = random.randrange(nb_movies)
        else:
            raise Exception("No more free movimons availables")
        return (Data._free_movies[nb_movies])

    def get_strengh(self):
        return self._strengh

    def get_movie(self, movie):
        if movie in Data._movies:
            return Data._movies[movie]
        else:
            raise Http404
    
    
    def move(self, dir='up'):
        if (dir == 'up'):
            Data.move_up()
        elif (dir == 'down'):
            Data.move_down()
        elif (dir == 'left'):
            Data.move_left()
        elif (dir == 'right'):
            Data.move_right()

    def move_up():
        if (Data._x > 0):
            Data._x -= 1
    
    def move_down():
        if (Data._x < settings.MOVIEMON_SETTINGS['SIZE'][0] - 1):
            Data._x += 1
    
    def move_left():
        if (Data._y != 0):
            Data._y -= 1

    def move_right():
        if (Data._y < settings.MOVIEMON_SETTINGS['SIZE'][1] - 1):
            Data._y += 1
    

    def decrease_balls(self):
        Data._balls -= 1
    
    def increase_balls(self, nb_balls):
        Data._balls += nb_balls

    def launch_ball(self, movie):
        if Data._balls > 0:
            Data._balls -= 1
            return True
        else:
            return False

    def capture_movie(self, movie):
        Data._free_movies.remove(movie)
        Data._capture_movies.append(movie)


    def get_slots():
        slots = {
                'a' : [0,0],
                'b' : [0,0],
                'c' : [0,0],
                }

        print(settings.MOVIEMON_SAVED_PATH)
        for slot in slots:
            files = glob.glob(settings.MOVIEMON_SAVED_PATH + "/slot" + slot + "_*_*.mmg" )
            if len(files) != 0:
                tmp = files[0].split('/')
                file = tmp.pop()
                name = file.split('.')
                slots[slot] = [name[0].split('_')[1], name[0].split('_')[2]]

        return (slots)
                
            
if __name__ == '__main__':
    
    data2 = Data()
    #data2.load("a")
    print("________ after load __________")
    print("data start state : " + str(data2._x))

    data2.move()
    data2.move()
    print(data2._x)
    data2.move()
    print("data :" + str(data2._x))

    #data2.capture_movie(data2.get_random_movie())
    data2.hard_save("a")
    print("free movies : " + str(data2._free_movies))
    print("capture movies : " + str(data2._capture_movies))
    
    print(Data.get_slots())