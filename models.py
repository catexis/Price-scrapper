from peewee import *
from playhouse.migrate import *
db = SqliteDatabase("price.db")

class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = db

class Hardware(BaseModel):
    """Модель для названий оборудования"""
    name = CharField()
    url = CharField(null = True)

class Price(BaseModel):
    """Модель для данных о ценах"""
    id_name = ForeignKeyField(Hardware)
    date = CharField()
    price_e = FloatField(null = True, default = 0)
    price_r = FloatField(null = True, default = 0)
    in_stock = BooleanField(null = True, default = False)



if __name__ == "__main__":
    db.create_tables([Hardware])
    db.create_tables([Price])
    # r = Hardware()
    # for i in r.select():
    #     print(i.name)
    # url = CharField(null = True)
    # migrator = SqliteMigrator(db)
    # migrate(
    #     migrator.add_column('hardware', 'url', url),
    # )