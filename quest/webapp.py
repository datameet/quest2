import web
from .db import Dataset
from .template import render_template
import os

urls = (
    "/", "index",
    "/schema/(.*)", "schema",
)
app = web.application(urls, globals())


class index:
    def GET(self):
        datasets = Dataset.find_all()
        return render_template("index.html", datasets=datasets)


class schema:
    """We want to serve the schema files under /schema/.
    """
    def GET(self, filename):
        if ".." in filename:
            raise web.notfound()

        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, "static", "schema", filename)
        print "path", path

        if not os.path.exists(path):
            raise web.notfound()

        web.header("Content-type", self.get_content_type(filename))
        return open(path).read()

    def get_content_type(self, filename):
        if filename.endswith(".jsonld"):
            return "application/ld+json"
        elif filename.endswith(".json"):
            return "application/json"
        else:
            return "application/octet-stream"
