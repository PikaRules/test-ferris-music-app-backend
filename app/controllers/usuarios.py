from ferris import Controller, route
from app.models.usuario import Usuario


class Usuarios(Controller):
	class Meta:
		View = 'json'
		prefixes = ('api',)


	#get all
	def list(self):
		usuarios = Usuario.all()
		self.context['data'] = usuarios

	def api_list(self):
		#self.response.headers['Access-Control-Allow-Origin'] = '*'
	    #self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
	    #self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		usuarios = Usuario.all()
		self.context['data'] = usuarios	

	@route
	def api_addNew( self, email, name ):
		newUser = Usuario( email = email, name = name )
		newUser.put()

	@route
	def api_getOne(self, email):
		self.context['data'] = Usuario.find_by_email( email )

	@route
	def api_updateOne(self):
		self.context['data'] =  self.request.params


