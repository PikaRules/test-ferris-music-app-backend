from ferris import BasicModel
from google.appengine.ext import ndb
from ferris import Controller, route, messages


class Song(BasicModel):

	title=ndb.StringProperty()
	artist=ndb.StringProperty()
	tags=ndb.StringProperty()
	album=ndb.StringProperty()

	@classmethod
	def all_songs(cls):
		# get all songs
		songs = ndb.gql( " SELECT * FROM Song" )
		return songs

	@classmethod
	def all_songs_by_artist(cls,artist_query=None):

		songs = ndb.gql( " SELECT * FROM Song WHERE artist=artist_query")
		return songs