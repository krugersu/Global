

# Импортируем библиотеку, соответствующую типу нашей базы данных 
# В данном случае импортируем все ее содержимое, чтобы при обращении не писать каждый раз имя библиотеки, как мы делали в первой статье
from peewee import *
import pysqlite3
from pathlib import Path 

pathDB = Path("data", "myDB.sqlite") 


all_db=pysqlite3.connect(pathDB)



class BaseModel(Model):
    class Meta:
        database = all_db  # соединение с базой, из шаблона выше

# Определяем модель исполнителя
class Artist(BaseModel):
    code = TextField(column_name='code', null=True)
    opcode = IntegerField(column_name='opcode', null=True)
    cquant = FloatField(column_name='cquant', null=True)

    class Meta:
        table_name = 'goodsitem'
        
        
