import sqlite3



class SharkSightingRepository:
    def __init__(self, connect: str):
        self.con = sqlite3.connect(connect)
        self.con.isolation_level = None
        self.cursor = con.cursor()
        if (':memory:' == connect):
            cur.executescript("""
                create table sharks(
                    id,
                    type,
                    latitude,
                    longitude,
                    timestamp
                );
                """)
