from fastapi import FastAPI
from pydantic import BaseModel
from starlette.status import HTTP_201_CREATED


class DemoModel(BaseModel):
    name: str


app = FastAPI()


@app.get('/hello')
async def api_get():
    return [{'name': 'Motto'}, {'name': 'Otto'}]


@app.get('/hello/{name}')
async def api_retrieve(name: str):
    return {'name': name}


@app.put('/hello', status_code=HTTP_201_CREATED)
async def api_put(payload: DemoModel):
    return payload.dict()
