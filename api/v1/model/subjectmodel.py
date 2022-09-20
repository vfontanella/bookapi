import peewee

from api.v1.utils.db import db

class Subject(peewee.Model):
    subject_id = peewee.PrimaryKeyField(null=False)
    subject = peewee.CharField()
    description = peewee.CharField(max_length=100)
    
    class Meta:
        database = db
        db_table = "subjects"
        order_by = ('subject',)
