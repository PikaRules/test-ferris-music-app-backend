from ferris import Controller, route, messages
from app.models.songtest import Songtest

class Hello(Controller):

	def list(self):

		salida = ""
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

		cosa = message.to_message( song1, SongtestMessage )

		return "<h1> hello </h1>"

	def queryTest():
		salida = ""
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

		cosa = message.to_message( song1, SongtestMessage )

		#print songs.count()
		#print songs
		#print listOfSongs

