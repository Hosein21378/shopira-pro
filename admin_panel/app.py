from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Shopira Pro Admin Panel")

templates = Jinja2Templates(directory="admin_panel/templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return """
    <html>
    <head><title>Shopira Pro - Admin Panel</title></head>
    <body style="background:#111; color:white; font-family:sans-serif; padding:40px;">
        <h1>پنل مدیریت Shopira Pro</h1>
        <p>پنل وب با موفقیت راه‌اندازی شد ✅</p>
        <p>در حال توسعه...</p>
    </body>
    </html>
    """
