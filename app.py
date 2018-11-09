from http_instance.Server import app
from Resources.resources import Holi
from http_instance.api import MainApi



def add_resources():
    api = MainApi(app)
    api.add_source(Holi, '/holi')



if __name__ == '__main__':
    add_resources()
    app.run()
