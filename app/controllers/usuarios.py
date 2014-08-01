from ferris import Controller
from app.models.usuario import Usuario

class Usuarios(Controller):
	class Meta:
		View = 'json'


	def list(self):
		#usuarios = Usuario.all()
		self.context['data'] = {'test':'test'}

	def add(self):
		return "sdfsdfdsfsdfs"

	def view(self, param):
		usuario = Usuario.find_all_by_property(email=param)
		self.context['data'] = usuario

	def edit(self):
		return "sdfsdfdsfsdfs"

	def delete(self):
		return "sdfsdfdsfsdfs"

