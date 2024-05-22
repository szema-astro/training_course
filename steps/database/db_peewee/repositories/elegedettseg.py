from peewee import fn
from steps.database.db_peewee.training_models import Elegedettseg


def get_all_elegedettseg():
    return Elegedettseg.select().dicts()


def filter_by_nps_group(nps_group):
    return (Elegedettseg
            .select()
            .where(Elegedettseg.nps_group == nps_group)
            .order_by(Elegedettseg.start_date.desc())
            .dicts())


def groupby_month_nps_group():
    return (Elegedettseg
            .select(
                Elegedettseg.nps_group,
                Elegedettseg.start_date_month,
                fn.AVG(Elegedettseg.duration).alias('duration_avg'),
                fn.SUM(Elegedettseg.nps).alias('nps_sum'),
                fn.AVG(Elegedettseg.nps).alias('nps_avg'),
            )
            .group_by(
                Elegedettseg.nps_group,
                Elegedettseg.start_date_month,
            )
            .dicts())
