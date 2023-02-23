from pymongo import MongoClient,DESCENDING
from entity.model import Sensordata
from usecase.get_sensordata import SensordataRepository
import os

url=os.environ['DB_string']
dbname=os.environ['DB_name']
collectionname=os.environ['DB_collection']

class SensordataDBInteractor(SensordataRepository):
    def get_latest_sensordata(self) -> Sensordata:
        def get_latest_sensordata_from_DB():
            client = MongoClient(url)
            db=client[dbname]
            collection=db[collectionname]
            envdata=[]
            document=collection.find_one(sort=[( 'time', DESCENDING )])
            envdata.append(Sensordata(**document))
            return envdata
        return get_latest_sensordata_from_DB()

