import click
from steps.database.db_peewee.training_models import mysql_db, get_all_models
from steps.database.db_peewee.training_schema_manager import create_all_tables, drop_all_tables


@click.group()
def cli():
    pass


@cli.command(help='Az összes tábla létrehozása a training adatbázisban, ha még nem léteznek.')
def create_all():
    create_all_tables()
    click.echo(f"Az összes tábla létrejött a {mysql_db.database} adatbázisban.")


@cli.command(help='Az összes tábla eltávolítása a training adatbázisból.')
def drop_all():
    drop_all_tables()
    click.echo(f'Az összes tábla törlésre került a {mysql_db.database} adatbázisból.')


@cli.command(help='Az összes definiált model lekérdezése.')
def get_models():
    for model in get_all_models():
        click.echo(model)


if __name__ == '__main__':
    cli()