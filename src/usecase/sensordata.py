from entity.model import Sensordata
from abc import ABCMeta, abstractmethod

# 抽象基底クラス(alternate interface)


class SensordataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_latest_sensordata(self) -> Sensordata:
        raise NotImplementedError

    def post_sensordata(self):
        raise NotImplementedError

# usecase/interactor


class SensordataUsecase():
    sensordata_repo: SensordataRepository

    def __init__(self, repo: SensordataRepository) -> None:
        self.sensordata_repo = repo

    def get_latest_sensordata(self) -> Sensordata:
        return self.sensordata_repo.get_latest_sensordata()

    def post_sensordata(self, sensordata):
        return self.sensordata_repo.post_sensordata(sensordata)
