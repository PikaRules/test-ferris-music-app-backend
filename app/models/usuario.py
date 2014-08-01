from ferris import BasicModel, ndb

class Usuario(BasicModel):
	email = ndb.StringProperty(required=True)
	name = ndb.StringProperty()

	@staticmethod
	def all():
		demall = ndb.gql( " SELECT * FROM Usuario" )
		return demall

	@staticmethod
	def find_by_email( email ):
		result = ndb.gql( " SELECT * FROM Songtest WHERE title = :1", email )
		return result