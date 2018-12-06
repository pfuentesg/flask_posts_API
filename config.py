import os

db = {
    "name": os.getenv('dbNAME', 'posts')
}
app = {
    'debug': os.getenv('app_debug', True),
    'environment': 'development',
    'host': '0.0.0.0',
    'port': '3030'
}

api = {
    'context': '/api'
}

logger = {
    'level': os.getenv('log_level', 'info')
}