import numpy as np
from pathlib import Path
from peewee import chunked
from file_handling.readers.reader import CsvReader
from training_models import mysql_db, Pod

project_root = Path(__file__).parent.parent.parent.parent
data_folder = project_root.joinpath('jupyter', '0_adatok')

reader = CsvReader()
reader.set_file_path(data_folder.joinpath('pod.csv').absolute())
reader.set_reader_config({'sep': ';'})
df = reader.to_dataframe()

column_name_map = {
    'Partnerszám': Pod.partnerszam.name,
    'Kapcsolatszám': Pod.kapcsolatszam.name,
    'POD': Pod.pod.name,
    'SM_nr': Pod.sm_nr.name,
    'Status': Pod.status.name,
    'Igény típusa': Pod.igeny_tipus.name,
    'Tipus': Pod.tipus.name,
    'Elvégzendő mun': Pod.elvegzendo_munka.name,
    'Csati_doksi_beerk_datum': Pod.dokumentum_beerkezes_datum.name,
    'Csati_doksi_ok_datum': Pod.dokumentum_ervenyes_datum.name,
    'Csati_doksi_nemok_datum': Pod.dokumentum_hibas_datum.name,
    'Keszrejelentes_datum': Pod.keszrejelentes_datum.name,
    'Merofel_kiadas_datum': Pod.merofel_kiadas_datum.name,
    'Merofel_progr_datum': Pod.merofel_progr_datum.name,
    'SM_COM_datum': Pod.sm_com_datum.name,
    'HH_szerzodes_kuldes_datum': Pod.hh_szerzodes_datum.name,
    'SM_nr_count': Pod.sm_nr_count.name,
    'Ügyfél azonosító': Pod.ugyfel_azonosito.name,
    'szerződés azonosító': Pod.szerzodes_azonosito.name,
    'ügyfél kategória': Pod.ugyfel_kategoria.name,
    'Szerződés Típusa': Pod.szerzodes_tipusa.name,
    'Szerződés értéke Ft-ban': Pod.szerzodes_erteke.name
}

df.rename(columns=column_name_map, inplace=True)
df.replace(np.nan, None, inplace=True)

Pod.truncate_table()
with mysql_db.atomic():
    for batch in chunked(df.to_dict(orient='records'), 500):
        Pod.insert_many(batch).execute()
