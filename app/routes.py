from ferris.core import routing, plugins
from app.controllers.usuarios import Usuarios
import webapp2


class HomeHandler(webapp2.RequestHandler):
    def get(self):
    	self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.write('This is the HomeHandler.')

# Routes all App handlers
#routing.auto_route()

routing.add(routing.Route('/home', HomeHandler))

# Default root route
#routing.default_root()