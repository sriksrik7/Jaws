import csv
from datetime import datetime

from SharkAttack import SharkAttack
from GpsCoordinates import GpsCoordinates
from dateutil import parser


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
                attackDateTime = getDateTime(row[1], row[13])
                if attackDateTime is None:
                    continue
                attack = SharkAttack(attackDateTime, row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                     row[10], row[11], row[12], row[14], row[15], row[16], row[17], row[18])
                attacks.append(attack)
                line_count += 1
    print(f'Processed {line_count} shark attacks')
    return attacks


def getDateTime(date: str, time: str) -> datetime:
    if date is None:
        return None
    try:
        return parser.parse(date + ' ' + time if time is not None else date)
    except Exception:
        return None

def getGpsCoordinates(location: str, area: str, country: str) -> GpsCoordinates:
    locationIndicators = []
    if location is not None:
        locationIndicators.append(location)
    if area is not None:
        locationIndicators.append(area)
    if country is not None:
        locationIndicators.append(country)
    if len(locationIndicators) is 0 or (len(locationIndicators) == 1 and locationIndicators[0] == country):
        return None
    return None
