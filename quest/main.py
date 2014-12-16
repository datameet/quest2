import web
from . import config

config.load_config()

from webapp import app

application = app.wsgifunc()

# Heroku doesn't handle static files, use StaticMiddleware.
application = web.httpserver.StaticMiddleware(application)
