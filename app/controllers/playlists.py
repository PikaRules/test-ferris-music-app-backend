from ferris import Controller
from app.models.playlist import Playlist

class Playlists(Controller):
	class Meta():
			View='json'

	def list(self):
		all_playlist=list(Playlist.all_playlist())
		self.context['data'] = all_playlist

	def add(self):
		playlist=Playlist(title=self.request.params["title"],songs=self.request.params["songs"])
		playlist.put()

	def delete(self):
		song=Song(title=self.request.params["title"],artist=self.request.params["artist"])
		song.put()		