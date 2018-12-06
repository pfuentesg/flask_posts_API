import os

db = {
    "name": os.getenv('dbNAME', 'posts')
}
app = {
    'debug': os.getenv('app_debug', True),
    'environment': 'development',
    'host': os.getenv('HOST', '0.0.0.0'),
    'port': os.getenv('PORT', '3030')
}

api = {
    'context': '/api'
}

logger = {
    'level': os.getenv('log_level', 'info')
}
