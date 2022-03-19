from fastapi import FastAPI
from app import scarper
from pydantic import BaseModel


class allinfo(BaseModel):
    url: str


app = FastAPI()


@app.get("/")
async def root():
    return "hello dear !"


@app.post("/allinfo/")
async def allinfo(item: allinfo):
    resp = scarper.AllInfo(item.url)
    return True
