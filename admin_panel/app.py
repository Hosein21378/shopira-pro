from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Shopira Pro Admin Panel")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return """
    <html>
    <head>
        <title>Shopira Pro - Admin Panel</title>
        <meta charset="UTF-8">
    </head>
    <body style="background:#111827; color:white; font-family:sans-serif; padding:50px; text-align:center;">
        <h1 style="font-size:42px; margin-bottom:20px;">🛍️ Shopira Pro</h1>
        <h2 style="color:#10b981;">پنل مدیریت با موفقیت راه‌اندازی شد ✅</h2>
        <p style="margin-top:30px; color:#9ca3af;">در حال توسعه...</p>
    </body>
    </html>
    """
