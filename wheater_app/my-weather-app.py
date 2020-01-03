import urllib.request
import argparse

apikey = 'e094c740a64137f63457b8352659613d'
fp = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=' + apikey)
mybytes = fp.read()
mystr = mybytes.decode('utf8')
fp.close()

print(mystr)

parser = argparse.ArgumentParser(description='Weather app #37462189')
parser.add_argument('--l', '-location', dest='location', default=None, type=str, help="Location by city")
parser.add_argument('--r', '-range', dest='range', choices=('day', 'week'), default='day', \
                    type=str, help="Range (week/day)")
parser.add_argument('--c', '-cords', nargs=2, dest='cords', type=float, \
                    help="Location by coordinates, 2 floats, lon&lat")
parser.add_argument('--d', '-celsius', action='store_false', default=False, dest='degrees',
                    help='Show Celsius degrees (default)') #false
parser.add_argument('--f', '-fahrenheit', action='store_true', default=False, dest='degrees',
                    help='Show  Fahrenheit degrees')


args = parser.parse_args()
print(args.cords)
