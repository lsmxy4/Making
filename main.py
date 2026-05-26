from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR/"app/templates")

@app.get("/",response_class=HTMLResponse)
def read_root(request : Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"title" : "북북"}
    )


@app.get("/search", response_class=HTMLResponse)
async def read_item(
    request: Request, q: Optional[str] = None):
    return templates.TemplateResponse(
        request, "index.html", {"keyword": q}
    )
