from ferris import Controller, route
from app.models.artist import Artist
from app.tools.request_helper import RequestHelper
import json
import sys


class Artists(Controller,RequestHelper):
	class Meta:
		View = 'json'
		prefixes = ('api',)


	@route
	def api_getAll(self):
		self.setCordsHeaders()
		artists = Artist.all()
		self.context['data'] = artists	

	@route
	def api_addNew( self ):
		self.setCordsHeaders()
		response = { "success": False , "error": "" }
		try:
			jsonObject = self.getPostDataObject()
			name = jsonObject.get('name','')
			sex = jsonObject.get('sex','')
			description = jsonObject.get('description','')
			self.context['data'] = jsonObject
			if name :
				newFoo = Artist( name = name, sex = sex, description = description )
				newFoo.put()
				response['success'] = True
			self.context['data'] = response
		except:
			response['success'] = False
			response['error'] = sys.exc_info()
			self.context['data'] = response