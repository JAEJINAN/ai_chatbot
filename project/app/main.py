from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # project directory

print(BASE_DIR)
app = FastAPI()


templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})



