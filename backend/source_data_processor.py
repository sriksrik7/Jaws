import csv
import traceback
from datetime import datetime

from backend import gps
from backend.attack import SharkAttack
from dateutil import parser


# Convert source csv to list of shark attacks (enriched with latitude/longitude)
def readSharkAttacksFromSourceCsv(csvFile: str) -> [SharkAttack]:
    attacks = []
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                attack = mapSourceCsvRowToSharkAttack(row)
                if attack is not None:
                    attacks.append(attack)
                line_count += 1
    print(f'Reviewed {line_count} shark attack entries. Got {len(attacks)} valid results with complete data.')
    return attacks


# Map source csv row to shark attack and enrich it with latitude/longitude data
def mapSourceCsvRowToSharkAttack(row: [str]) -> SharkAttack:
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
    gpsLocation = Gps.getGpsLocation(location, area, country)
    if gpsLocation is None:
        return None

    latitude = gpsLocation.latitude
    longitude = gpsLocation.longitude
    address = gpsLocation.address

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
    link = row[17]

    return SharkAttack(id, dateTime, latitude, longitude, address, type, activity, name, age, sex, injury, fatal,
                       species, source, link)


# Write list of shark attacks to csv in our own cleaner format (including latitude/longitude enrichment)
def writeSharkAttacksToCsv(sharkAttacks: [SharkAttack], csvFile: str):
    with open(csvFile, 'w', newline='') as f:
        writer = csv.writer(f)
        for s in sharkAttacks:
            try:
                writer.writerow(
                    [s.id, s.datetime, s.latitude, s.longitude, s.address, s.type, s.activity, s.name, s.sex, s.age,
                     s.injury, s.fatal, s.species, s.source, s.link])
            except BaseException:
                traceback.print_exc()


# Convert date/time strings to a datetime object
def getDateTime(date: str, time: str) -> datetime:
    if date is None:
        return None
    try:
        return parser.parse(date + ' ' + time if time is not None else date)
    except Exception:
        return None
