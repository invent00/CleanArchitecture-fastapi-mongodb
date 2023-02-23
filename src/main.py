from fastapi import FastAPI
from gateway.mongodb_repo import SensordataDBInteractor
from usecase.get_sensordata import SensordataUsecase
from entity.model import Sensordata,Post_Sensordata

app = FastAPI()
# Controller
@app.get("/")
def read_root():
  test=SensordataUsecase(SensordataDBInteractor()).get_latest_sensordata()
  return test
@app.post("/sensordata")
def postenvdata(envdata:Post_Sensordata):
  status=SensordataUsecase(SensordataDBInteractor()).post_sensordata(envdata)
  return status

test=SensordataUsecase(SensordataDBInteractor()).get_latest_sensordata()
print(test)