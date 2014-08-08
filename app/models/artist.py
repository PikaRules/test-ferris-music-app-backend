from ferris import BasicModel, ndb

class Artist(BasicModel):
	name = ndb.StringProperty(required=True)
	sex = ndb.StringProperty( choices=( 'male','female' ) )
	description = ndb.StringProperty()

	@staticmethod
	def all():
		items = ndb.gql( " SELECT * FROM Artist" )
		return items

	@staticmethod
	def find_by_name( name ):
		result = ndb.gql( " SELECT * FROM Artist WHERE name = :1", name )
		return result