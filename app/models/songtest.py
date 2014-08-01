from ferris import BasicModel, messages
from google.appengine.ext import ndb

class Songtest(BasicModel):
	title = ndb.StringProperty(required=True)

class SongtestMessage(message.Message):
	title = message.StringField(1)
	

