from flask_restful import Api



class MainApi():
    def __init__(self, app):
        self.api = Api(app, '/api')
        # TODO: change this literal to config

    def add_source(self, resource, path):
        self.api.add_resource(resource, path)

