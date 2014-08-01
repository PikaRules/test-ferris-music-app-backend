from ferris import BasicModel
from google.appengine.ext import ndb

class Album(BasicModel):
	title = ndb.StringProperty()