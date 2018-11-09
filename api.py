from flask_restful import Api
from flask import Blueprint
from resources import Holi
from app import app


class MainApi():
    def __init__(self, app):
        self.api = Api(app)


    def add_source(self, resource, path):
        self.api.add_resource(resource, path)


MainApi(app).add_source(Holi, '/holi')
app.run()