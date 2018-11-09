from flask import Blueprint
from flask_restful import Resource
mod = Blueprint('resource', __name__, url_prefix='/')
@mod.route('/')
def get():
    return 'holi!'

class Holi(Resource):
    def get(self):
        return 'holi from instance'