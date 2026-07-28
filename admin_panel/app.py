from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Shopira Pro Admin Panel")

app.mount("/static", StaticFiles(directory="admin_panel/static"), name="static")
templates = Jinja2Templates(directory="admin_panel/templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return """
    <h1>پنل مدیریت Shopira Pro</h1>
    <p>در حال ساخت...</p>
    """
