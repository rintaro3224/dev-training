from fastapi import FastAPI
from pydantic import BaseModel
from machine_learning import predictOnAPI
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
    

@app.post('/api/titanic', response_model=SchemaOfTitanicFeaturesRequest)
def get_titanic_features(request_body: SchemaOfTitanicFeaturesRequest):
    return request_body