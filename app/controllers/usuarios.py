from ferris import Controller, route
from app.models.usuario import Usuario
import json


class Usuarios(Controller):
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
		self.response.headers['Access-Control-Allow-Origin'] = '*'
		self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		usuarios = Usuario.all()
		self.context['data'] = usuarios	

	@route
	def api_addNew( self ):
		self.response.headers['Access-Control-Allow-Origin'] = '*'
		self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		email = self.request.POST.get('email')
		name = self.request.POST.get('name')
		if ( email and  name ):
			newUser = Usuario( email = email, name = name )
			newUser.put()
		

	@route
	def api_getOne(self, email):
		self.response.headers['Access-Control-Allow-Origin'] = '*'
		self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		self.context['data'] = Usuario.find_by_email( email )

	@route
	def api_updateOne(self):
		self.response.headers['Access-Control-Allow-Origin'] = '*'
		self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		self.context['data'] =  self.request.params


