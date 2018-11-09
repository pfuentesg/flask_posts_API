from flask_restful import  Api
from flask import  Blueprint
from resources import  Holi
from app import  app
api = Api(app)
api.add_resource(Holi, '/holi')

app.run(

