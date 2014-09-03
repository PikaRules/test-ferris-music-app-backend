
from ferris import Controller, route
from app.models.usuario import Usuario
from app.tools.request_helper import RequestHelper
import json
import sys


class Test(Controller,RequestHelper):
	class Meta:
		View = 'json'
		prefixes = ('api',)

	@route
	def api_getAll(self):
		self.setCordsHeaders()
		self.context['data'] = 'Hola'	