from dotenv import dotenv_values
import pandas as pd
import pymysql
from pymysql import cursors
import random
import string

letters = string.ascii_lowercase
config = dotenv_values()


def connect_to_mysql():
    return pymysql.connect(
        host=config['MYSQL_HOST'],
        port=int(config['MYSQL_PORT']),
        db=config['MYSQL_DATABASE'],
        user=config['MYSQL_USERNAME'],
        password=config['MYSQL_PASSWORD'],
        charset='utf8mb4',
        cursorclass=cursors.DictCursor
    )


def create_sample_table(connection):
    sql = (
        "CREATE TABLE IF NOT EXISTS sample_table ("
        "id int(11) NOT NULL AUTO_INCREMENT, "
        "string_value varchar(255) COLLATE utf8mb4_hu_0900_ai_ci NOT NULL, "
        "float_value float(8, 3) NOT NULL, "
        "int_value int(11) NOT NULL, "
        "PRIMARY KEY (`id`) "
        ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hu_0900_ai_ci "
        "AUTO_INCREMENT=1;"
    )

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)


def generate_random_record():
    result_str = ''.join(random.choice(letters) for i in range(12))
    random_float = random.uniform(1, 6000)
    random_integer = random.randint(1, 30000)
    return result_str, random_float, random_integer


def insert_random_data(connection, record_number=60):
    with connection:
        with connection.cursor() as cursor:
            for indx in range(0, record_number):
                parameters = generate_random_record()
                print(f"{indx}:  VALUES ('{parameters[0]}', {parameters[1]:.3f}, {parameters[2]});")
                sql = (
                    "INSERT INTO sample_table "
                    "(string_value, float_value, int_value) "
                    f" VALUES ('{parameters[0]}', {parameters[1]:.3f}, {parameters[2]});"
                )
                cursor.execute(sql)
        connection.commit()


def is_empty_table(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT count(id) as rows_number FROM sample_table;")
            result = cursor.fetchone()
            return result['rows_number'] == 0


create_sample_table(connect_to_mysql())
if is_empty_table(connect_to_mysql()):
    insert_random_data(connect_to_mysql(), 80)


with connect_to_mysql() as connection:
    with connection.cursor() as cursor:
        query = "SELECT * FROM sample_table WHERE int_value between 121 and 1210;"
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(result)

        print(result)
        print(df.shape)
        print(df.info())
        print(df.head())
