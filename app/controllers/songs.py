from ferris import Controller, route, ndb
from app.models.artist import Artist
from app.models.song import Song
from app.tools.request_helper import RequestHelper
import json
import sys


class Songs(Controller,RequestHelper):
	class Meta:
		View = 'json'
		prefixes = ('api',)


	@route
	def api_getAll(self):
		self.setCordsHeaders()
		songs = Song.all()
		self.context['data'] = songs	

	@route
	def api_addNew( self ):
		self.setCordsHeaders()
		try:
			jsonObject = self.getPostDataObject()
			artist_key = ndb.Key( jsonObject['artist']['__kind__'], jsonObject['artist']['__id__'] )
			self.context['data'] = artist_key
			myArtist = artist_key.get()
			song_title = jsonObject['song']['title']
			song_description = jsonObject['song']['description']
			newFoo = Song( title = song_title, description = song_description, artist = myArtist )
			newFoo.put()
			"""description = jsonObject.get('description','')
			self.context['data'] = jsonObject
			if name :
				newFoo = Song( name = name, description = description )
				newFoo.put()"""
		except:
			self.context['data'] = sys.exc_info()