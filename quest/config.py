import web
import os

config = {
    "db_parameters": dict(dbn="postgres", db="quest", user=os.getenv('USER'), pw='')
}

def load_config():
    if 'DATABASE_URL' in os.environ:
        config['database_url'] = os.environ['DATABASE_URL']
    web.config.update(config)
    print config

