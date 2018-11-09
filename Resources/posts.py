from flask_restful import Resource


class Posts(Resource):
    def get(self):
        return 'posts GET'

    def post(self):
        return 'posts POST'

    def patch(self):
        return 'posts patch'

    def delete(self):
        return 'posts delete'
