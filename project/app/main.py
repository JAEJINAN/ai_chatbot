from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

BASE_DIR = Path(__file__).resolve().parent  # project directory
print(BASE_DIR)
print(BASE_DIR)
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory=BASE_DIR)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("templates/main.html", {"request": request,
                                                              "title": "영한챗봇"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)