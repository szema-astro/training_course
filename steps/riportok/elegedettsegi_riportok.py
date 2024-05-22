from steps.database.db_peewee.repositories.elegedettseg import (
    get_all_elegedettseg,
    filter_by_nps_group,
    groupby_month_nps_group
)
from steps.database.db_peewee.repositories.serializer import DataFrameSerializer

serializer = DataFrameSerializer(filter_by_nps_group, {'nps_group': 'Promoter'})
df = serializer.execute()
print(df.head())

serializer.function = get_all_elegedettseg
serializer.parameters = None
osszes_elegedettseg_df = serializer.execute()
print(osszes_elegedettseg_df.head(100))

serializer.function = groupby_month_nps_group
elegedettseg_aggr_df = serializer.execute()
print(elegedettseg_aggr_df)
