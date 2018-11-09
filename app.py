from flask import Flask
from resources import mod
app = Flask(__name__)

app.register_blueprint(mod)


if __name__ == '__main__':
    app.run()
