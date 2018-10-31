import configparser
import os

from flask_pymongo import PyMongo
from waterberry.utils.logger import logger
from waterberry.db.electrovalve_dao import ElectrovalveDAO
from waterberry.db.raspberry_dao import RaspberryDAO
from waterberry.db.dht_sensor_dao import DHTSensorDAO
from waterberry.utils.definition import ROOT_DIR

file = os.path.join(ROOT_DIR, 'config/waterberry.config')
config = configparser.ConfigParser()
config.read_file(open(file))

database = PyMongo()

class DaoFactory:
    def __init__(self):
        self.configuration = os.environ['PLATFORM']

    def initApp(self, app):
        app.config['MONGO_HOST'] = config.get(self.configuration, 'MONGO_HOST')
        app.config['MONGO_PORT'] = config.getint(self.configuration, 'MONGO_PORT')
        app.config["MONGO_DBNAME"] = config.get(self.configuration, 'MONGO_DBNAME')
        database.init_app(app, config_prefix='MONGO')
        database.app = app
        return app

    def createElectrovalveDAO(self):
        return ElectrovalveDAO(database)

    def createRaspberryDAO(self):
        return RaspberryDAO(database)

    def createDHTSensorDAO(self):
        return DHTSensorDAO(database)
