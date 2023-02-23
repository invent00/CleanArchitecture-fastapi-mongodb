from pydantic import BaseModel, Field
from datetime import datetime,timezone,timedelta
from typing import List,Optional
from bson.objectid import ObjectId

#timezone setting
JST=timezone(timedelta(hours=+9),"JST")
UTC=timezone(timedelta(hours=+9),"UTC")

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Sensordata(BaseModel):
    id:Optional[PyObjectId]=Field(alias='_id')    
    time:datetime=Field(description="時刻")
    temp:float=Field(description="温度 ℃")
    humid:float=Field(description="湿度 %")
    light:float=Field(description="光度 lx")
    pressure:float=Field(description="気圧 hPa")
    noise:float=Field(description="騒音 dB")
    eCO2:float=Field(description="CO2濃度推定値 ppm")
    class Config:
        arbitrary_types_allowed=True
        json_encoders={
            ObjectId:str
        }

class Post_Sensordata(BaseModel):
    time:datetime=Field(description="時刻")
    temp:float=Field(description="温度 ℃")
    humid:float=Field(description="湿度 %")
    light:float=Field(description="光度 lx")
    pressure:float=Field(description="気圧 hPa")
    noise:float=Field(description="騒音 dB")
    eCO2:float=Field(description="CO2濃度推定値 ppm")
    class Config:
        arbitrary_types_allowed=True
        json_encoders={
            ObjectId:str
        }