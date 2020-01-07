import urllib.request
import argparse
from collections import Counter

apikey = '2ae04d95d78eb539f7b8cce05a16f9e5'


def top():
    line_list = [this_line.rstrip('\n') for this_line in open('Locations.txt')]
    l_sorted = Counter(line_list).most_common()
    try:
        print('Most popular cities:')
        print(l_sorted[0][0])
        print(l_sorted[1][0])
        print(l_sorted[2][0])
    except IndexError:
        pass
    exit()


parser = argparse.ArgumentParser(description='Weather app #37462189')
subparsers = parser.add_subparsers()
parser.add_argument('--l', '-location', dest='location', default=None, type=str, help='Location by city')
parser.add_argument('--r', '-range', dest='range', choices=('day', 'week'), default='day', \
                    type=str, help='Range (week/day)')
parser.add_argument('--c', '-cords', nargs=2, dest='cords', type=str, \
                    help='Location by coordinates, 2 floats, lon&lat')
parser.add_argument('--d', '-celsius', action='store_false', default=False, dest='degrees',
                    help='Show Celsius degrees (default)')  # false
parser.add_argument('--f', '-fahrenheit', action='store_true', default=False, dest='degrees',
                    help='Show  Fahrenheit degrees')
parser.add_argument('--q', '-resent', dest='resent',
                    help='Show  N resent towns, or 0 for all locations')
parser_top = subparsers.add_parser('top', help='list of 3 favorite cities')
parser_top.set_defaults(func=top)

args = parser.parse_args()
try:
    args.func()
except AttributeError:
    pass
q = ''
if args.resent is not None:
    try:
        with open('Locations.txt', 'r') as f:
            lines = f.read().splitlines()
            line = lines[-int(args.resent):-1]
            line.append(lines[-1])
            print(line)
    except IndexError:
        print('Please enter the location')
if args.cords is not None:
    q = 'http://api.openweathermap.org/data/2.5/weather?lat=' + args.cords[0] + '&lon=' + args.cords[
        1] + '&appid=' + apikey
if args.location is not None:
    q = 'http://api.openweathermap.org/data/2.5/weather?q=' + args.location + '&APPID=' + apikey
    try:
        fp = urllib.request.urlopen(q)
        mybytes = fp.read()
        mystr = mybytes.decode('utf8')
        fp.close()
    except urllib.error.HTTPError:
        print('Wrong city!')
        exit()
    if mystr == '{"cod": 500,"message": "Internal server error"}':
        print('Wrong city!')
        exit()
    else:
        print(mystr)
        f = open('Locations.txt', 'a+')
        f.write(args.location + '\n')
        f.close()
        exit()
if (args.cords is None) and (args.location is None) and (args.resent is None):
    try:
        with open('Locations.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            print(last_line)
    except IndexError:
        print('Please enter the location')

# fp = urllib.request.urlopen(q)
# mybytes = fp.read()
# mystr = mybytes.decode('utf8')
# fp.close()
# print(mystr)

# print(args.cords, args.location, args.range)
