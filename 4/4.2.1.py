import psycopg2


class DataBaseConnector:
    def __init__(self, db_name, host, port, user, password):
        self.db_name = db_name
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(database=self.db_name, user=self.user, password=self.password, host=self.host,
                                         port=self.port)
        except psycopg2.Error as err:
            raise psycopg2.Error(f'Database Error: unable to connect to the database due to:\n{err}')
        return self.conn

    def execute_query(self, query):
        cursor = self.__enter__().cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def __exit__(self, cursor, exc_type, esc_val, exc_tb):
        cursor.close()
        self.conn.close()


if __name__ == "__main__":
    a = DataBaseConnector(db_name='countries', host='10.10.30.252', port='5432', user='postgres',
                          password='p0S+gre')
    print(a.execute_query('SELECT a.name, a.population FROM "public"."Capital" as a WHERE '
                          'a.population>10000000 LIMIT 10;'))
    print(a.execute_query('SELECT b.name FROM "public"."Country" as b WHERE b.population<50000 '
                          'ORDER BY b.name DESC LIMIT 10;'))
