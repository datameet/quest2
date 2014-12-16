import web
from .db import Dataset
from .template import render_template

urls = (
    "/", "index"
)
app = web.application(urls, globals())

class index:
    def GET(self):
        datasets = Dataset.find_all()
        return render_template("index.html", datasets=datasets)


