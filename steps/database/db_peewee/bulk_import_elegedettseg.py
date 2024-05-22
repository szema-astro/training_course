import numpy as np
from pathlib import Path
from peewee import chunked
from file_handling.readers.reader import CsvReader
from training_models import mysql_db, Elegedettseg

project_root = Path(__file__).parent.parent.parent.parent
data_folder = project_root.joinpath('jupyter', '0_adatok')

reader = CsvReader()
reader.set_file_path(data_folder.joinpath('elegedettseg.csv').absolute())
reader.set_reader_config({'sep': ';'})
df = reader.to_dataframe()

column_name_map = {
    'StartDate': Elegedettseg.start_date.name,
    'EndDate': Elegedettseg.end_date.name,
    'Duration (in seconds)': Elegedettseg.duration.name,
    'NPS_NPS_GROUP': Elegedettseg.nps_group.name,
    'NPS': Elegedettseg.nps.name,
    'Rendeles': Elegedettseg.rendeles.name,
    'UP': Elegedettseg.up.name
}

df.rename(columns=column_name_map, inplace=True)
df.replace(np.nan, None, inplace=True)
df[Elegedettseg.start_date_month.name] = df[Elegedettseg.start_date.name].to_numpy().astype('datetime64[M]')

Elegedettseg.truncate_table()
with mysql_db.atomic():
    for batch in chunked(df.to_dict(orient='records'), 500):
        Elegedettseg.insert_many(batch).execute()
