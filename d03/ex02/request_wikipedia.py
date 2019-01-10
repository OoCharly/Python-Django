import sys, requests, json, dewiki

def search_wiki(str):
    url = "https://fr.wikipedia.org/w/api.php"
    payload = {"action": "parse",
               "format": "json",
               "errorformat": "bc",
               "page": str,
               "prop": "wikitext",
               "formatversion": "latest"}
    response = requests.get(url, params=payload)
    if response.status_code != 200:
        raise Exception("Erreur HTTP: " + str(response.status_code))
    elif response.json().get('error'):
        raise Exception("Erreur: " + response.json().get('error')['info'])
    else:
        res = dewiki.from_string(response.json().get('parse')['wikitext'])
        print(res)
        try:
            with open(response.json().get('parse')['title'].replace(' ', '_') + ".wiki", "w") as file:
                file.write(res)
        except PermissionError as e:
            print(e)
            exit(1)


def usage():
    print("usage: python3 request_wikipedia.py <your_request>")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            search_wiki(sys.argv[1])
        except Exception as e:
            print(e)
    else:
        usage()
