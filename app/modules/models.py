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
	selected_post = (Posts.select()
		.where(Posts.validated == 1)
		.order_by(fn.Random())
		.limit(1)[0]
	)
	return selected_post

def check_for_post(gfy_url):
	query = Posts.get(Posts.url == gfy_url)
	return query
