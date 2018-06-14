import time
from datetime import datetime

from waterberry.db.dao_factory import database, DaoFactory
from waterberry.gpio.board import Board
from waterberry.utils.logger import logger

def ManualElectrovalve(electrovalve_id):
    with database.app.app_context():
        electrovalve_dao = DaoFactory().createElectrovalveDAO()
        gpio_dao = DaoFactory().createGPIODAO()
        board = Board()

        electrovalve = electrovalve_dao.getElectrovalveById(electrovalve_id)
        electrovalve_pin = gpio_dao.getPinByName(electrovalve['electrovalve_pin'])

        logger.info('ManualElectrovalve job started ...')
        logger.info('Water electrovalve with id {} at pin {}'.format(electrovalve_id, electrovalve_pin))

        electrovalve['watering'] = True
        electrovalve_dao.updateElectrovalveById(electrovalve, electrovalve_id)

        board.initBoard()
        board.setupOutputPin(electrovalve_pin)
        board.enablePin(electrovalve_pin)

        logger.info('watering for ... {} seconds'.format(electrovalve['duration']))
        time.sleep(electrovalve['duration'])

        board.disablePin(electrovalve_pin)
        electrovalve['watering'] = False
        electrovalve['last_water'] = datetime.utcnow()
        electrovalve_dao.updateElectrovalveById(electrovalve, electrovalve_id)