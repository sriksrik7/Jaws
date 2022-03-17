from datetime import datetime

from geopy.location import Location


class SharkAttack:
    def __init__(self, id: str, datetime: datetime, location: Location, type: str, activity: str, name: str, sex: str,
                 age: str, injury: str, fatal: str, species: str, source: str, hrefFormula: str, href: str):
        self.id = id
        self.datetime = datetime
        self.location = location
        self.type = type
        self.activity = activity
        self.name = name
        self.sex = sex
        self.age = age
        self.injury = injury
        self.fatal = fatal
        self.species = species
        self.source = source
        self.hrefFormula = hrefFormula
        self.href = href

    def __repr__(self):
        return "datetime: {0}\nlatitude: {1}\nlongitude: {2}\ntype: {3}\nage: {4}\nsex: {5}\ninjury: {6}\nfatal: {7}" \
               "\nspecies: {8}\nsource: {9}\nhrefFormula: {10}\nhref: {11}\n".format(
            self.datetime, self.location.latitude, self.location.longitude, self.type, self.age, self.sex,
            self.injury, self.fatal, self.species, self.source, self.hrefFormula, self.href)
