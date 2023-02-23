from pymongo import MongoClient, DESCENDING
from entity.model import Sensordata
from usecase.sensordata import SensordataRepository
import os

url = os.environ['DB_string']
dbname = os.environ['DB_name']
collectionname = os.environ['DB_collection']


class SensordataDBInteractor(SensordataRepository):
    def get_latest_sensordata(self) -> Sensordata:
        def get_latest_sensordata_from_DB():
            client = MongoClient(url)
            db = client[dbname]
            collection = db[collectionname]
            envdata = []
            document = collection.find_one(sort=[('time', DESCENDING)])
            envdata.append(Sensordata(**document))
            return envdata
        return get_latest_sensordata_from_DB()

    def post_sensordata(self, sensordata):
        def post_sensordata_to_DB(sensordata: Sensordata):
            client = MongoClient(url)
            db = client[dbname]
            collection = db[collectionname]
            cursor = collection.insert_one(sensordata.dict(by_alias=True))
            if cursor.inserted_id:
                status = "inserted data"
            else:
                status = "some error occur"
            return status
        return post_sensordata_to_DB(sensordata)
