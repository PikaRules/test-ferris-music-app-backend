from ferris import Controller, route
import json


class RequestHelper:
	def setCordsHeaders( self ):
		self.response.headers['Access-Control-Allow-Origin'] = '*'
		self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, dataType'

	def getPostDataObject( self ):
		jsonstring = self.request.body.replace( "'",'"').replace("\'",'"')
		jsonObject = json.loads(  jsonstring  ) 
		return jsonObject