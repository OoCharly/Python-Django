import sys

def capital_city(state):
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

    if state in states.keys():
        print(capital_cities[states[state]])
    else:
        print("Unknown State")

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        capital_city(arg)