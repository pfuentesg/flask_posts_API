from flask import Flask
from container import config
class local_server(Flask):

    def process_response(self, response):
        response.headers['server'] = None
        return response

app = local_server(__name__)
app.debug = config.app['debug']
