from flask_restful import Api
from container import config


class MainApi():
    def __init__(self, app):
        self.api = Api(app, config.api['context'])

    def add_source(self, resource, path):
        self.api.add_resource(resource, path)

