import psycopg2


class DataBaseConnector:
    def __init__(self, db_name: str, host: str, port: str, user: str, password: str, query): # если ты используешь
        # аннотации - использу их везде
        self.db_name = db_name
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.query = query  # плохое решение загнать и запрос и коннект в инит

    def __enter__(self):
        self.conn = psycopg2.connect(database=self.db_name, user=self.user, password=self.password, host=self.host,
                                     port=self.port)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, esc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    with DataBaseConnector(db_name='countries', host='10.10.30.252', port='5432', user='postgres',
                           password='p0S+gre', query='SELECT * FROM "public"."Capital" LIMIT 10') as a:
        print(a)
