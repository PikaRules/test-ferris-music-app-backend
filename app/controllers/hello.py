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

	@route
	def jquery(self):
		html = '<!doctype html>'
		html += '<html>'
		html += '<head>'
		html += '<meta charset="utf-8" />'
		html += '<title>Demo</title>'
		html += '</head>'
		html += '<body>'
		html += '<a href="http://jquery.com/">jQuery</a>'
		html += '<script src="jquery.js"></script>'
		html += '<script>'
		html += '</script>'
		html += 'que onda!'
		html += '</body>'
		html += '</html>'

		return html
	
