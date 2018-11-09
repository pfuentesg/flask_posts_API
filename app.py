from Server import app
from resources import Holi
from api import MainApi



def add_resources():
    api = MainApi(app)
    api.add_source(Holi, '/holi')



if __name__ == '__main__':
    add_resources()
    app.run()
