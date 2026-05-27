from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path
from motor.motor_asyncio import AsyncIOMotorClient

from app.models import mongodb
from app.models.books import BookModel

app = FastAPI()


BASE_DIR=Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR/ "templates")


@app.get("/",response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(
        keyword="python",
        public = "sdh",
        price = 1200,
        image = "me.png"
    )
    save_book = await mongodb.engine.save(book)
    print(save_book.model_dump)
    return templates.TemplateResponse(
        request,
        "index.html",
        {"title":"북북"}
    ) 


@app.get("/search",response_class=HTMLResponse)
async def read_item(request:Request,q:str):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"keyword":q}
    )


@app.on_event("startup")
async def on_app_start():
    print("hello server")
    mongodb.connect()

@app.on_event("shutdown")
async def on_app_shutdown():
    print("goodbye server")
    mongodb.close()
