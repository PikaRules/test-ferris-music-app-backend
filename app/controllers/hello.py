from ferris import Controller, route, messages
from google.appengine.ext import ndb
from app.models.songtest import Songtest

class Hello(Controller):
	class Meta:
			View = 'json'


	def list(self):

		song1 = Songtest( title = "song1" )
		song1.put()
		song2 = Songtest( title = "song2" )
		song2.put()
		song3 = Songtest( title = "song3" )
		song3.put()
		song4 = Songtest( title = "song4" )
		song4.put()

		listOfSongs = []
		listOfSongs.append( song1 )
		listOfSongs.append( song2 )

		songs = ndb.gql( " SELECT * FROM Songtest" )

		self.context['data'] = songs

	@route	
	def cosa(self):
		return "hey"

	
