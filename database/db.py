import psycopg2
from psycopg2 import Error
from psycopg2.extensions import AsIs
import configparser
import os # Access environmental variables

class Database:
    def __init__(self):
        self.user = os.environ['PG_MASTER_USERNAME']
        self.passwd = os.environ['PG_MASTER_PASSWORD']
        self.host = os.environ['PG_MASTER_HOST']
        self.port = os.environ['PG_MASTER_PORT']
        self.db = os.environ['PG_MASTER_NAME']

    def connect_set(self, dict_val, table_name):
        columns = dict_val.keys()
        values = [dict_val[column] for column in columns]
        sql = 'insert into ' + table_name + '(%s) values %s'
        conn = None
        try:
            conn = psycopg2.connect(
                user=self.user, password=self.passwd, host=self.host, port=self.port, database=self.db)
            cursor = conn.cursor()
            
            cursor.execute(sql, (AsIs(','.join(columns)), tuple(values)))
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(conn):
                cursor.close()
                conn.close()