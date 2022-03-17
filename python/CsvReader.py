import csv
import ssl
from datetime import datetime

import certifi
import geopy.geocoders
from SharkAttack import SharkAttack
from dateutil import parser
from geopy.geocoders import Nominatim
from geopy.location import Location

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent='Shark-Attack', scheme='https', timeout=10)


def getSharkAttacks(csvFile: str) -> [SharkAttack]:
    attacks = []
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                attack = mapSharkAttack(row)
                if attack is not None:
                    attacks.append(attack)
                line_count += 1
    print(f'Reviewed {line_count} shark attack entries. Got {len(attacks)} valid results with complete data.')
    return attacks


def mapSharkAttack(row: [str]) -> SharkAttack:
    # Get date time
    date = row[1]
    time = row[13]
    dateTime = getDateTime(date, time)
    if dateTime is None:
        return None

    # Get gps location
    country = row[4]
    area = row[5]
    location = row[6]
    gpsLocation = getGpsLocation(location, area, country)
    if gpsLocation is None:
        return None

    id = row[0]
    type = row[3]
    activity = row[7]
    name = row[8]
    sex = row[9]
    age = row[10]
    injury = row[11]
    fatal = row[12]
    species = row[14]
    source = row[15]
    hrefFormula = row[16]
    href = row[17]

    return SharkAttack(id, dateTime, gpsLocation, type, activity, name, age, sex, injury, fatal, species, source, hrefFormula, href)


def getDateTime(date: str, time: str) -> datetime:
    if date is None:
        return None
    try:
        return parser.parse(date + ' ' + time if time is not None else date)
    except Exception:
        return None


# https://stackoverflow.com/questions/5807195/how-to-get-coordinates-of-address-from-python
def getGpsLocation(location: str, area: str, country: str) -> Location:
    locationIndicators = []
    if location is not None:
        locationIndicators.append(location)
    if area is not None:
        locationIndicators.append(area)

    if len(locationIndicators) == 0 or (len(locationIndicators) == 1 and locationIndicators[0] == country):
        return None

    allLocators = ', '.join(locationIndicators)
    print('Getting coordinates for: ' + allLocators)
    #location = geolocator.geocode('35 Sunset Drive, Chatham NJ', exactly_one=True)
    return geopy.location.Location(address='', point='40.7081443,-74.4263388', raw='')
