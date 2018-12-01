from flask_restful import reqparse

def validate_patch_post():
    parser = reqparse.RequestParser()
    parser.add_argument('content', required=True, help='content of the post')
    return parser.parse_args()
