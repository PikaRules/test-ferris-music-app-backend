from ferris import BasicModel, ndb

class Usuario(BasicModel):
	email = ndb.StringProperty(required=True)
	playlists = ndb.StringProperty()

	@staticmethod
	def all():
		demall = ndb.gql( " SELECT * FROM Usuario" )
		return demall