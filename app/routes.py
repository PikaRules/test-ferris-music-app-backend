from ferris.core import routing, plugins
from app.controllers.usuarios import Usuarios

# Routes all App handlers
routing.auto_route()


# Default root route
#routing.default_root()