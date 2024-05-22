import pandas as pd
import pymysql
from pymysql import cursors
from dotenv import dotenv_values


class MysqlConnection(object):
    def __init__(self):
        self.connector = None

    def __enter__(self):
        config = dotenv_values()
        self.connector = pymysql.connect(
            host=config['MYSQL_HOST'],
            port=int(config['MYSQL_PORT']),
            db=config['MYSQL_DATABASE'],
            user=config['MYSQL_USERNAME'],
            password=config['MYSQL_PASSWORD'],
            charset='utf8mb4',
            cursorclass=cursors.DictCursor
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self.connector.commit()
        else:
            self.connector.rollback()
        self.connector.close()

    def query_to_dataframe(self, query):
        with self.connector.cursor() as cursor:
            cursor.execute(query)
            return pd.DataFrame(cursor.fetchall())
