from fastapi import FastAPI
from pydantic import BaseModel
from machine_learning.titanic import PredictOnAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/helloworld")
def get_hello_message():
    return {"message": "Hello World!"}

@app.get('/api/{message}')
def get_any_message(message: str):
    return {"message": message}

class SchemaOfTitanicFeaturesRequest(BaseModel):
    Sex:str
    Pclass:str
    Age:int
    Parch:int
    SibSp:int
    

@app.post('/api/titanic')
def get_titanic_features(request_body: SchemaOfTitanicFeaturesRequest):
    survival_probability = PredictOnAPI.derive_survival_probability(
        Sex=request_body.Sex,
        Pclass=request_body.Pclass,
        Age=request_body.Age,
        Parch=request_body.Parch,
        SibSp=request_body.SibSp
    )
    return {"survival_probability": survival_probability}