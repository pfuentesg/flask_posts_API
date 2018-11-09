from flask_restful import Api



class MainApi():
    def __init__(self, app):
        self.api = Api(app)


    def add_source(self, resource, path):
        self.api.add_resource(resource, path)

