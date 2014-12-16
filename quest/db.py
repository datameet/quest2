import web

if "database_url" in web.config:
    db = web.database(web.config.database_url)
else:
    db = web.database(**web.config.db_parameters)

class Dataset(web.storage):
    def __init__(self, id, data):
        self.id = id
        self.update(data)

    @staticmethod
    def find_all():
        rows = db.select("dataset")
        return [Dataset(row.id, row.data) for row in rows]