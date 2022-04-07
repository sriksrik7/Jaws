from datetime import datetime

import geopy.distance


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
        input_location = (latitude, longitude)
        attack_location = (self.latitude, self.longitude)
        mileDistance = geopy.distance.geodesic(input_location, attack_location).miles
        print("distance between {0}, {1} and {2}, {3} is {4} miles".format(latitude, longitude, self.latitude, self.longitude, mileDistance))
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
