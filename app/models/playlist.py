from ferris import BasicModel
from google.appengine.ext import ndb
from ferris import Controller, route, messages
from app.models.song import Song

class Playlist(BasicModel):
	title=ndb.StringProperty()
	songs=ndb.StructuredProperty(Song, repeated=True)

	@classmethod
	def all_playlist(cls):
		# get all songs
		playlists=ndb.gql(" SELECT * FROM Playlist")
		return playlists

	@classmethod
	def all_playlist_by_user(cls,user=None):
		pass
