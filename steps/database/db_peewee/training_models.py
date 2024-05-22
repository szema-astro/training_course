import sys
import inspect

from dotenv import dotenv_values
from peewee import MySQLDatabase
from peewee import Model, BigAutoField, CharField, DateField, DateTimeField, IntegerField

config = dotenv_values()
mysql_db = MySQLDatabase(
    config['MYSQL_DATABASE'],
    host=config['MYSQL_HOST'],
    port=int(config['MYSQL_PORT']),
    user=config['MYSQL_USERNAME'],
    password=config['MYSQL_PASSWORD'],
    charset='utf8mb4',
    autoconnect=True,
)


def get_all_models(just_name=True):
    classes = []
    for cls_name, cls_obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        if issubclass(cls_obj, BaseModel) and cls_name != BaseModel.__name__:
            classes.append(cls_name if just_name else cls_obj)
    return classes


class BaseModel(Model):
    class Meta:
        database = mysql_db


class Elegedettseg(BaseModel):
    id = BigAutoField(primary_key=True)
    start_date = DateTimeField()
    end_date = DateTimeField()
    duration = IntegerField()
    nps_group = CharField(max_length=100)
    nps = IntegerField()
    rendeles = IntegerField(null=True)
    up = IntegerField(null=True)
    start_date_month = DateField(null=True)


class Pod(BaseModel):
    id = BigAutoField(primary_key=True)
    partnerszam = IntegerField(null=True, help_text='Partnerszám')
    kapcsolatszam = IntegerField(null=True, help_text='Kapcsolatszám')
    pod = CharField(max_length=100, null=True)
    sm_nr = IntegerField(null=True, help_text='SM_nr')
    status = CharField(max_length=50, null=True)
    igeny_tipus = CharField(max_length=50, null=True, help_text='Igény típusa')
    tipus = CharField(max_length=50, null=True, help_text='Tipus')
    elvegzendo_munka = CharField(max_length=100, null=True, help_text='Elvégzendő munka')
    dokumentum_beerkezes_datum = DateField(null=True, help_text='Csati_doksi_beerk_datum')
    dokumentum_ervenyes_datum = DateField(null=True, help_text='Csati_doksi_ok_datum')
    dokumentum_hibas_datum = DateField(null=True, help_text='Csati_doksi_nemok_datum')
    keszrejelentes_datum = DateField(null=True, help_text='Készrejelentés dátum')
    merofel_kiadas_datum = DateField(null=True, help_text='Merofel_kiadas_datum')
    merofel_progr_datum = DateField(null=True, help_text='Merofel_progr_datum')
    sm_com_datum = DateField(null=True, help_text='SM_COM_datum')
    hh_szerzodes_datum = DateField(null=True, help_text='HH_szerzodes_kuldes_datum')
    sm_nr_count = IntegerField(null=True, help_text='SM_nr_count')
    ugyfel_azonosito = IntegerField(null=True, help_text='Ügyfél azonosító')
    szerzodes_azonosito = IntegerField(null=True, help_text='szerződés azonosító')
    ugyfel_kategoria = CharField(max_length=50, null=True, help_text='ügyfél kategória')
    szerzodes_tipusa = CharField(max_length=100, null=True, help_text='Szerződés Típusa')
    szerzodes_erteke = IntegerField(null=True, help_text='Szerződés értéke Ft-ban')
