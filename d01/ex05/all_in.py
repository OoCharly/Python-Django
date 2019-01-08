import sys

def trim_args(args):
    states = {
        "Oregon"    :   "OR",
        "Alabama"   :   "AL",
        "New Jersey" :   "NJ",
        "Colorado"  :   "CO"
    }

    capital_cities = {
        "OR" : "Salem",
        "AL" : "Montgomery",
        "NJ" : "Trenton",
        "CO" : "Denver"
    }

    arg_list = args.split(',')

    for arg in arg_list:
        var = arg.title().strip()
        if var:
            if var in states.keys():
                print("{0} is the capital of {1}".format(capital_cities[states[var]], var))
            elif var in capital_cities.values():
                for key in capital_cities.keys():
                    if var == capital_cities[key]:
                        for state in states.keys():
                            if key == states[state]:
                                print("{0} is the capital of {1}".format(var, state))
            else:
                print("{0} is neither a capital city nor a state".format(var))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        trim_args(sys.argv[1])
