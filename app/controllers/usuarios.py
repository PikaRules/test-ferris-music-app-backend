from ferris import Controller, route
from app.models.usuario import Usuario

class Usuarios(Controller):
	class Meta:
		View = 'json'


	#get all
	def list(self):
		usuarios = Usuario.all()
		self.context['data'] = usuarios

	@route
	def addNew( self, email, name ):
		newUser = Usuario( email = email, name = name )
		newUser.put()

	@route
	def getOne(self, email):
		self.context['data'] = Usuario.find_by_email( email )

	@route
	def updateOne(self):
		self.context['data'] =  self.request.params


