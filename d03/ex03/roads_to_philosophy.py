import sys, requests
from bs4 import BeautifulSoup


def get_link(html):
    req = ''
    intro = html.find(id="mw-content-text").find_all(lambda tag: tag.name == 'p' and not tag.has_attr('class'))
    for p in intro:
        for link in p.find_all(lambda tag: tag.name == 'a' and not tag.has_attr('class') and tag.has_attr('href')):
            req = link['href'].replace("/wiki/", '')
            if ':' not in req and '/' not in req and '#' not in req:
                break
        if req != '':
            break
    if req != '':
        return req
    else:
        raise Exception("It leads to a dead end !")


def take_road(req):
    pages = []
    while req.lower() != 'philosophy':
        url = "https://en.wikipedia.org/wiki/" + req
        res = requests.get(url, allow_redirects=False)
        if res.status_code == 404:
            raise Exception("It leads to a dead end !")
        elif res.status_code == 301:
            res = requests.get(url)
            for red in res.history:
                if red.url.replace('https://en.wikipedia.org/wiki/', '') not in pages:
                    pages.append(res.url.replace('https://en.wikipedia.org/wiki/', ''))
                else:
                    raise Exception('It leads to an infinite loop !')
        elif res.status_code != 200:
            raise Exception("Erreur HTTP: " + str(res.status_code))
        elif req in pages:
            raise Exception('It leads to an infinite loop !')
        else:
            pages.append(res.url.replace('https://en.wikipedia.org/wiki/', ''))
        html = BeautifulSoup(res.text, 'html.parser')
        req = get_link(html)
    for page in pages:
        print(page)
    print(str(len(pages)) + " road(s) from " + pages[0] + " to philosophy!")


def usage():
    print("usage: python3 roads_to_philosophy.py <your_request>")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            take_road(sys.argv[1])
        except Exception as e:
            print(e)
    else:
        usage()
