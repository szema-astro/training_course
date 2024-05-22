import pandas as pd
from steps.database.db_driver.connection import MysqlConnection


with MysqlConnection() as conn:
    with conn.connector.cursor() as cursor:
        query = "SELECT * FROM pod"
        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall())
        print(df.head())


with MysqlConnection() as conn:
    with conn.connector.cursor() as cursor:
        query = "SELECT * FROM pod WHERE dokumentum_hibas_datum IS NOT NULL"
        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall())
        print(df.head())

pod_df = None
hibas_df = None
with MysqlConnection() as conn:
    pod_df = conn.query_to_dataframe("SELECT * FROM pod")
    hibas_df = conn.query_to_dataframe(
        "SELECT * FROM pod WHERE dokumentum_hibas_datum IS NOT NULL ORDER BY dokumentum_hibas_datum DESC"
    )

print(pod_df.head())
print(pod_df.info())
