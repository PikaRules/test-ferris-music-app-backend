from ferris import BasicModel
from google.appengine.ext import ndb
from ferris import Controller, route, messages
from app.models.artist import Artist


class Song(BasicModel):

	title=ndb.StringProperty(required=True)
	description = ndb.StringProperty()
	artist=ndb.StructuredProperty( Artist )

	@classmethod
	def all(self):
		songs = ndb.gql( " SELECT * FROM Song" )
		return songs

	@classmethod
	def find_by_title(self,title):
		songs = ndb.gql( " SELECT * FROM Song WHERE title = :1", title )
		return songs