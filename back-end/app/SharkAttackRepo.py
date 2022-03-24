import sqlite3

from app.Csv import getSharkAttacksFromProcessedCsv
from app.SharkAttack import SharkAttack


class SharkAttackRepo:
    def __init__(self, connect: str):
        self.con = sqlite3.connect(connect, check_same_thread=False)
        self.con.isolation_level = None
        if (':memory:' == connect):
            self.createSharkAttackTable()

    def add(self, sharkAttack: SharkAttack):
        insertStatement = """
            insert into sharks (id, datetime, latitude, longitude, address, type, activity, name, sex, age, injury, fatal, species, source, link)
            values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}');
            """.format(sanitize(sharkAttack.id), sanitize(sharkAttack.datetime), sanitize(sharkAttack.latitude),
                       sanitize(sharkAttack.longitude), sanitize(sharkAttack.address), sanitize(sharkAttack.type),
                       sanitize(sharkAttack.activity), sanitize(sharkAttack.name), sanitize(sharkAttack.sex),
                       sanitize(sharkAttack.age), sanitize(sharkAttack.injury), sanitize(sharkAttack.fatal),
                       sanitize(sharkAttack.species), sanitize(sharkAttack.source), sanitize(sharkAttack.link))
        self.__executeStatement(insertStatement)

    def addAllCsv(self, csvFile: str):
        for attack in getSharkAttacksFromProcessedCsv(csvFile):
            self.add(attack)

    def getAll(self) -> [SharkAttack]:
        return self.__executeQuery("""
            select * from sharks;
            """)

    def createSharkAttackTable(self):
        self.__executeScript("""
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
                injury,
                fatal,
                species,
                source,
                link                                                                                
            );
            """)

    def __executeScript(self, script: str):
        print('Executing: ' + script)
        cursor = self.con.cursor()
        cursor.executescript(script)

    def __executeStatement(self, statement: str):
        print('Executing: ' + statement)
        cursor = self.con.cursor()
        cursor.execute(statement)

    def __executeQuery(self, query: str) -> [SharkAttack]:
        print('Querying: ' + query)
        cursor = self.con.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        attacks = []
        for row in rows:
            attacks.append(self.__mapRowToSharkAttack(row))
        return attacks

    def __mapRowToSharkAttack(self, row) -> SharkAttack:
        id = row[0]
        datetime = row[1]
        latitude = row[2]
        longitude = row[3]
        address = row[4]
        type = row[5]
        activity = row[6]
        name = row[7]
        age = row[8]
        sex = row[9]
        injury = row[10]
        fatal = row[11]
        species = row[12]
        source = row[13]
        link = row[14]
        return SharkAttack(id, datetime, latitude, longitude, address, type, activity, name, sex, age, injury,
                           fatal, species, source, link)


def sanitize(data: str) -> str:
    return data.replace("'", "''")
