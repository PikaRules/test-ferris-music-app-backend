from ferris import BasicModel
from google.appengine.ext import ndb
from ferris import Controller, route, messages
from app.models.artist import Artist


class Song(BasicModel):

	title=ndb.StringProperty(required=True)
	description = ndb.StringProperty()
	artist = ndb.KeyProperty( kind = Artist )

	@classmethod
	def all(self):
		query_songs = ndb.gql( " SELECT * FROM Song" )
		songs = query_songs.map( self.all_callback, limit=100 )
		return songs

	@classmethod
	def find_by_title(self,title):
		query_songs = ndb.gql( " SELECT * FROM Song WHERE title = :1", title )
		songs = query_songs.map( self.all_callback, limit=100 )
		return songs

    #https://developers.google.com/appengine/docs/python/ndb/async#tasklets
	@ndb.tasklet
	def all_callback(song):
		msong = {}
		if song.artist is not None:
			tartist = yield song.artist.get_async()
			msong =  parse_song( song, tartist )
			raise ndb.Return(msong)
		else:
			msong = parse_song( song, None )
			raise ndb.Return(msong)


def parse_song( song , artist ):
	msong = {}
	martist = {}
	if artist is not None:
		martist["__kind__"] = artist.key.kind()
		martist["__id__"] = artist.key.id()
		martist["name"] = artist.name
		martist["description"] = artist.description
		martist["sex"] = artist.sex
	msong["artist"] = martist
	msong["__kind__"] = song.key.kind()
	msong["__id__"] = song.key.id()
	msong["title"] = song.title
	msong["description"] = song.description
	return msong