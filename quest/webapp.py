import web

urls = (
    "/", "index"
)
app = web.application(urls, globals())
application = app.wsgifunc()

class index:
    def GET(self):
        return "Hello, world!\n"


