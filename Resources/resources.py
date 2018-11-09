from flask_restful import Resource


class Holi(Resource):
    def get(self):
        return 'holi from instance'