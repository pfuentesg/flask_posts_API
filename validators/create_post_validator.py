from flask_restful import reqparse

def validate_post_post():
    parser = reqparse.RequestParser()
    parser.add_argument('content', required=True, help='content of the post')
    parser.add_argument('author', required=True, help='Author of the post')
    return parser.parse_args()
