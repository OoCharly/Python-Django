import sys, antigravity


def iscoordinate(lat, long):
    if lat in range(-90, 90) and long in range(-180, 180):
        return True
    return False

def do_the_geohash():
    lat = float(input('Latitude(float): '))
    long = float(input('Longitude(float): '))
    if iscoordinate(lat, long):
        dow = input('DateDow(AAAA-MM-DD-DOW): ')
        antigravity.geohash(lat, long, bytes(dow, 'UTF-8'))
    else:
        print("Wrong coordinates")
        print("Latitude between -90 and 90 degrees.")
        print("Longitude between -180 and 180 degrees")
        do_the_geohash()



def usage():
    print("Latitude between -90 and 90 degrees.")
    print("Longitude between -180 and 180 degrees")
    print("Datedow format: YYYY-MM-DD-dow")
    print("Dow can be the day of week (example 'thursday').")
    exit(1)


if __name__=="__main__":
    try:
        do_the_geohash()
    except Exception as e:
        print(e)
        usage()
