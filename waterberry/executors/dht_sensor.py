import time
from datetime import datetime

from waterberry.db.dao_factory import database, DaoFactory
from waterberry.gpio.dht_sensor import DHTSensor
from waterberry.utils.logger import logger

def DHTSensorExecutor():
    with database.app.app_context():
        dht_sensor_dao = DaoFactory().createDHTSensorDAO()
        dht_sensor_dao.initSensor()
        gpio_dao = DaoFactory().createGPIODAO()

        dht_sensor = DHTSensor(dht_sensor_dao, gpio_dao)
        humidity, temperature = dht_sensor.readData()
        dht_sensor.setData(humidity, temperature)