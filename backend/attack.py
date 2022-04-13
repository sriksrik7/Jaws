import math
from datetime import datetime


class SharkAttack:
    def __init__(self, id: str, datetime: datetime, latitude: float, longitude: float, address: str, type: str,
                 activity: str, name: str, sex: str, age: str, injury: str, fatal: str, species: str, source: str,
                 link: str):
        self.id = id
        self.datetime = datetime
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.type = type
        self.activity = activity
        self.name = name
        self.sex = sex
        self.age = age
        self.injury = injury
        self.fatal = fatal
        self.species = species
        self.source = source
        self.link = link

    def isWithinRadius(self, latitude: float, longitude: float, mileRadius: int):
        mileDistance = get_distance(latitude, longitude, self.latitude, self.longitude)
        print("distance between {0}, {1} and {2}, {3} is {4} miles".format(latitude, longitude, self.latitude,
                                                                           self.longitude, mileDistance))
        return mileRadius > mileDistance

    def serialize(self):
        return {"id": self.id,
                "datetime": self.datetime,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "address": self.address,
                "type": self.type,
                "activity": self.activity,
                "sex": self.sex,
                "age": self.age,
                "injury": self.injury,
                "fatal": self.fatal,
                "species": self.species,
                "source": self.source,
                "link": self.link}

    def __repr__(self):
        return "datetime: {0}\naddress: {1}\nlatitude: {2}\nlongitude: {3}\ntype: {4}\nage: {5}\nsex: {6}\ninjury: {7}\nfatal: {8}" \
               "\nspecies: {9}\nsource: {10}\nlink: {11}\nid:{12}".format(
            self.datetime, self.address, self.latitude, self.longitude, self.type, self.age, self.sex,
            self.injury, self.fatal, self.species, self.source, self.link, self.id)


def get_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    R = 6372800  # Earth radius in meters

    #defend against bad types
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a)) * 0.00062137
