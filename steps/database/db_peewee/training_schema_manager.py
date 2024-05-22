from .training_models import mysql_db, get_all_models


def create_all_tables():
    mysql_db.create_tables(get_all_models(just_name=False))


def drop_all_tables():
    mysql_db.drop_tables(get_all_models(just_name=False))
