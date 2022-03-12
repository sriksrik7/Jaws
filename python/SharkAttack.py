from datetime import datetime


class SharkAttack:
    def __init__(self, datetime: datetime, type: str, country: str, area: str, location: str,
                 activity: str, name: str, sex: str, age: str, injury: str, fatal: str, species: str,
                 source: str, pdf: str, hrefFormula: str, href: str):
        self.datetime = datetime
        self.type = type
        self.country = country
        self.area = area
        self.location = location
        self.activity = activity
        self.name = name
        self.sex = sex
        self.age = age
        self.injury = injury
        self.fatal = fatal
        self.species = species
        self.source = source
        self.pdf = pdf
        self.hrefFormula = hrefFormula
        self.href = href

    def __repr__(self):
        return "datetime: {0}\ntype: {1}\ncountry: {2}\narea: {3}\nage: {4}\nsex: {5}\ninjury: {6}\nfatal: {7}" \
               "\nspecies: {8}\nsource: {9}\npdf: {10}\nhrefFormula: {11}\nhref: {12}\nlocation: {13}\n".format(
            self.datetime, self.type, self.country, self.area, self.age, self.sex, self.injury,
            self.fatal, self.species, self.source, self.pdf, self.hrefFormula, self.href, self.location)
