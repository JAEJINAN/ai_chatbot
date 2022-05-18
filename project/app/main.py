from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent  # project directory

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR)

current_time = f'{datetime.now().hour: >2} : {datetime.now().minute: >2}'
print(current_time)


# 메인(로딩) 화면
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("templates/index.html",
                                      {"request": request,
                                       "title": "영한챗봇",
                                       "time": current_time})


# 채팅창
@app.get('/chattings', response_class=HTMLResponse)
async def chattings(request: Request):
    return templates.TemplateResponse("templates/chattings.html", {"request": request,
                                                                   "time": current_time, })
    
@app.get('/chattings/mic', response_class=HTMLResponse)
async def on_mic(request: Request):
    
    return templates.TemplateResponse("templates/chattings.html", {"request": request,
                                                                   "time": current_time, })
    


# 비디오 화면
@app.get('/videos', response_class=HTMLResponse)
async def videos(request: Request):
    return templates.TemplateResponse("templates/videos.html", {"request": request,
                                                                "video_url": "https://www.youtube.com/embed/GjsB6GcbcN8",
                                                                "time": current_time, })


# 유저화면
@app.get('/users', response_class=HTMLResponse)
async def users(request: Request):
    return templates.TemplateResponse("templates/users.html", {"request": request,
                                                               "time": current_time, })


# 채팅 내용 확인
@app.get('/chatlogs', response_class=HTMLResponse)
async def chatlogs(request: Request):
    return templates.TemplateResponse("templates/chatlogs.html", {"request": request,
                                                                  "time": current_time, })


# 감정 요약 화면
# @app.get('/summaries', response_class=HTMLResponse)
# async def chatlogs(request: Request):
#     return templates.TemplateResponse("templates/summaries.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
