import sqlite3

from app.SharkAttack import SharkAttack


class SharkAttackRepo:
    def __init__(self, connect: str):
        self.con = sqlite3.connect(connect)
        self.con.isolation_level = None
        self.cursor = self.con.cursor()
        if (':memory:' == connect):
            self.createSharkAttackTable()

    def add(self, sharkAttack: SharkAttack):
        self.cursor.executescript("""
            insert into sharks (id, datetime, latitude, longitude, address, type, activity, name, sex, age, injury, fatal, species, source, link)
            values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14});
            """.format(sharkAttack.id, sharkAttack.datetime, sharkAttack.latitude, sharkAttack.longitude,
                       sharkAttack.address, sharkAttack.type, sharkAttack.activity, sharkAttack.name, sharkAttack.sex,
                       sharkAttack.age, sharkAttack.injury, sharkAttack.fatal, sharkAttack.species, sharkAttack.source,
                       sharkAttack.link))

    def getAll(self) -> [SharkAttack]:
        return self.cursor.executescript("""
            select * from sharks;
            """)

    def createSharkAttackTable(self):
        self.cursor.executescript("""
            create table sharks(
                id,
                datetime,
                latitude,
                longitude,
                address,
                type,
                activity,
                name,
                sex,
                age,   
                inury,
                fatal,
                species,
                source,
                link                                                                                
            );
            """)
