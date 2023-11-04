#uvicorn main:app --reload
from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app=FastAPI()

@app.get("/search/{m}")
async def search_wiki(m: str, r: int = 7):
    return wikipedia.search(m, results=r)

@app.get("/summary/{n}")
async def summary_wiki(n: str):
    return wikipedia.summary(n)

class search_from_wiki(BaseModel):
    object: str
    results: int = 1

@app.post("/search_wiki/")
async def search_wikipedia(d: search_from_wiki):
    return wikipedia.search(d.object, results=d.results)





















                 



























