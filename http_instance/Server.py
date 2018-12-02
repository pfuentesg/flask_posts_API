from flask import Flask

class local_server(Flask):

    def process_response(self, response):
        response.headers['server'] = None
        return response

app = local_server(__name__)
