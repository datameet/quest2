import web
import logging

def setup_logging():
    FORMAT = "%(asctime)-15s [%(levelname)s] %(message)s"
    logging.basicConfig(level=logging.INFO, format=FORMAT)


app = web.auto_application()
application = app.wsgifunc()

setup_logging()
logger = logging.getLogger(__name__)

from . import config
logger.info("loading config")
config.load_config()

from webapp import app
application = app.wsgifunc()

# Heroku doesn't handle static files, use StaticMiddleware.
application = web.httpserver.StaticMiddleware(application)
