from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI(title="Shopira Pro MiniApp")

app.mount("/static", StaticFiles(directory="miniapp/static"), name="static")
templates = Jinja2Templates(directory="miniapp/templates")

@app.get("/", response_class=HTMLResponse)
async def miniapp_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/shop", response_class=HTMLResponse)
async def shop_page(request: Request):
    return templates.TemplateResponse("shop.html", {"request": request})

# TODO: اضافه کردن API endpoints برای ارتباط با ربات
