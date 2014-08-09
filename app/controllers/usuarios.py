from ferris import Controller, route
from app.models.usuario import Usuario
from app.tools.request_helper import RequestHelper
import json
import sys


class Usuarios(Controller,RequestHelper):
	class Meta:
		View = 'json'
		prefixes = ('api',)


	#get all
	def list(self):
		self.response.headers['Access-Control-Allow-Origin'] = '*'
		#self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		usuarios = Usuario.all()
		self.context['data'] = usuarios


    #self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
	def api_list(self):
		self.response.headers['Access-Control-Allow-Origin'] = '*'
		self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		usuarios = Usuario.all()
		self.context['data'] = usuarios	

	@route
	def api_getAll(self):
		self.setCordsHeaders()
		usuarios = Usuario.all()
		self.context['data'] = usuarios	

	@route
	def api_addNew( self ):
		self.setCordsHeaders()
		response = { "success": False , "error": "" }
		try:
			jsonObject = self.getPostDataObject()
			email = jsonObject['email']
			name = jsonObject['name']
			self.context['data'] = jsonObject
			if ( email and  name ):
				newUser = Usuario( email = email, name = name )
				newUser.put()
				response['success'] = True
			self.context['data'] = response
		except:
			response['success'] = False
			response['error'] = sys.exc_info()
			self.context['data'] = response
		

	@route
	def api_getOne(self, email):
		self.setCordsHeaders()
		self.context['data'] = Usuario.find_by_email( email )

	@route
	def api_updateOne(self):
		self.setCordsHeaders()
		self.context['data'] =  self.request.params