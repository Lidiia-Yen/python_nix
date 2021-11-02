import psycopg2


class DataBaseConnector:
    def __init__(self, db_name, host, port, user, password):
        self.db_name = db_name
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def __enter__(self):
        self.conn = psycopg2.connect(database=self.db_name, user=self.user, password=self.password, host=self.host,
                                     port=self.port)
        return self.conn

    def __exit__(self, exc_type, esc_val, exc_tb):
        self.conn.close()


if __name__ == "__main__":
    with DataBaseConnector(db_name='countries', host='10.10.30.252', port='5432', user='postgres',
                           password='p0S+gre') as a:
        cursor = a.cursor()
        cursor.execute('SELECT * FROM "public"."Capital" LIMIT 10')
        print(cursor.fetchall())
        cursor.close()
