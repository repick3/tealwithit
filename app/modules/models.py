from peewee import *
import datetime

db = SqliteDatabase('teal.db')

class BaseModel(Model):
    class Meta:
        database = db

class Posts(BaseModel):
	post = PrimaryKeyField()
	create_dt = DateTimeField()
	title = CharField(max_length=140)
	url = CharField(max_length=350)
	nws = BooleanField(default=False)
	validated = BooleanField(default=False)



def get_random_post():
	return Posts.select().order_by(fn.Random()).limit(1)[0]