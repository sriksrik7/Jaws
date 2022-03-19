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

    def __repr__(self):
        return "datetime: {0}\naddress: {1}\nlatitude: {2}\nlongitude: {3}\ntype: {4}\nage: {5}\nsex: {6}\ninjury: {7}\nfatal: {8}" \
               "\nspecies: {9}\nsource: {10}\nlink: {11}\nid:{12}".format(
            self.datetime, self.address, self.latitude, self.longitude, self.type, self.age, self.sex,
            self.injury, self.fatal, self.species, self.source, self.link, self.id)
