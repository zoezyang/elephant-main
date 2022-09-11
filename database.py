import psycopg2, psycopg2.extras


class Database():
    def __init__(self):
        self.conn = psycopg2.connect(
            database = 'postgres',
            host = "test2.cngdawjw4nxb.ap-southeast-2.rds.amazonaws.com",
            password = "A6NtbKHGzDt9kvB", 
            user = 'postgres',
            port = '5432'
        )
    
    def createTable(self):
        c = self.conn.cursor(cursor_factory= psycopg2.extras.DictCursor)
        with self.conn:
            c.execute("""CREATE TABLE reperfusion (
                reperfusion_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                activation_datetime datetime,
            )
            """)

    def createTableDemographics(self):
        c = self.conn.cursor(cursor_factory= psycopg2.extras.DictCursor)
        with self.conn:
            c.execute("""CREATE TABLE demographics (
                urn text PRIMARY KEY,
                first_name text,
                last_name text,
                dob text
            )
            """)

    def getAllDemographics(self):
        c = self.conn.cursor(cursor_factory= psycopg2.extras.DictCursor)
        with self.conn:
            c.execute("""select * from demographics""")
            return c.fetchall()

    def addPatient(self, urn, first_name, last_name, dob):
        c = self.conn.cursor(cursor_factory= psycopg2.extras.DictCursor)
        with self.conn:
            c.execute("""INSERT INTO demographics (urn, first_name, last_name, dob)
                VALUES (%s, %s, %s, %s)
                """, (urn, first_name, last_name, dob))

    def deletePatient(self, urn):
        c = self.conn.cursor(cursor_factory= psycopg2.extras.DictCursor)
        with self.conn:
            c.execute("""DELETE FROM demographics WHERE urn = %s """, (urn,))


if __name__== "__main__":
    db = Database()
    # db.createTableDemographics()
    # db.addPatient(101010, "Yop", "Yop", "2022-06-22")
    db.addPatient(111111, "O'Reilly", "O'Keefe", "2000-01-01")
    
