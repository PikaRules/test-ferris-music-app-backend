from ferris import Controller
from app.models.song import Song

class Songs(Controller):
	class Meta():
		View='json'

	def list(self):
		all_songs=Song.all_songs()
		self.context['data'] = all_songs

	def add(self):
		song=Song(title=self.request.params["title"],artist=self.request.params["artist"],tags=self.request.params["artist"],album=self.request.params["album"])
		song.put()

	def delete(self):
		song=Song(title=self.request.params["title"],artist=self.request.params["artist"])
		song.put()		