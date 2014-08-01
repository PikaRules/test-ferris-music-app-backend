from ferris import Controller
from app.models.usuario import Usuario

class Usuarios(Controller):
	class Meta:
		View = 'json'


	def list(self):
		usuarios = Usuario.all()
		self.context['data'] = usuarios

	def add(self):
		self.context['data'] = self.request.params

	def view(self, email):
		self.context['data'] = self.request.params

	def edit(self):
		return "sdfsdfdsfsdfs"

	def delete(self):
		self.context['data'] = self.request.params

