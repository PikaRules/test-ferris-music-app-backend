from ferris import BasicModel, ndb

class Usuario(BasicModel):
	email = ndb.StringProperty(required=True)
