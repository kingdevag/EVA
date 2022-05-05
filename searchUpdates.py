import configparser
from database import db

class UpdateC():

    config = configparser.ConfigParser()
    config.read('config.ini')
    ActualVersion = config['DEFAULT']['VERSION']

    def getVersion(param):
        collection = db["update"]
        PVU = collection.find_one()["UPDATE"][param]
        return PVU

    NewVersion = getVersion('VERSION')
    State = getVersion("STATE")
    URL = getVersion("URL")

    if ActualVersion < NewVersion:
        update = True
    else:
        update = False
    