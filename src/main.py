from fastapi import FastAPI
from gateway.mongodb_repo import SensordataDBInteractor
from usecase.get_sensordata import SensordataUsecase

app = FastAPI()
# Controller
@app.get("/")
def read_root():
  test=SensordataUsecase(SensordataDBInteractor()).get_latest_sensordata()
  return test

test=SensordataUsecase(SensordataDBInteractor()).get_latest_sensordata()
print(test)