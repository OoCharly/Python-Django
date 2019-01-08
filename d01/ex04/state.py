import sys

def capital_city(capital):
    states = {
        "Oregon"    :   "OR",
        "Alabama"   :   "AL",
        "NewJersey" :   "NJ",
        "Colorado"  :   "CO"
    }

    capital_cities = {
        "OR" : "Salem",
        "AL" : "Montgomery",
        "NJ" : "Trenton",
        "CO" : "Denver"
    }

    if capital in capital_cities.values():
        for key in capital_cities.keys():
            if capital == capital_cities[key]:
                for state in states.keys():
                    if key == states[state]:
                        print(state)
    else:
        print("Unknown capital city")

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        capital_city(arg)