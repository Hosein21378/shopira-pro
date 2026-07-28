from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import async_session
from database.models import User, Product, Transaction
import os
from datetime import datetime

app = FastAPI(title="Shopira Pro - Admin Panel")

app.mount("/static", StaticFiles(directory="admin_panel/static"), name="static")
templates = Jinja2Templates(directory="admin_panel/templates")

# ====================== Dependency ======================
async def get_db():
    async with async_session() as session:
        yield session

# ====================== Routes ======================

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, db: AsyncSession = Depends(get_db)):
    # آمار ساده
    total_users = await db.scalar("SELECT COUNT(*) FROM users")
    total_products = await db.scalar("SELECT COUNT(*) FROM products")
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "total_users": total_users or 0,
        "total_products": total_products or 0,
        "active_tab": "dashboard"
    })

@app.get("/users", response_class=HTMLResponse)
async def users_page(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM users ORDER BY created_at DESC")
    users = result.fetchall()
    return templates.TemplateResponse("users.html", {
        "request": request,
        "users": users,
        "active_tab": "users"
    })

@app.get("/products", response_class=HTMLResponse)
async def products_page(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM products")
    products = result.fetchall()
    return templates.TemplateResponse("products.html", {
        "request": request,
        "products": products,
        "active_tab": "products"
    })

@app.get("/financial", response_class=HTMLResponse)
async def financial_page(request: Request):
    return templates.TemplateResponse("financial.html", {
        "request": request,
        "active_tab": "financial"
    })

@app.post("/financial")
async def save_financial(
    card_number: str = Form(...),
    card_owner: str = Form(...),
    sheba: str = Form("")
):
    # در آینده این اطلاعات را در دیتابیس ذخیره می‌کنیم
    return RedirectResponse("/financial?success=1", status_code=303)

@app.get("/backups", response_class=HTMLResponse)
async def backups_page(request: Request):
    return templates.TemplateResponse("backups.html", {
        "request": request,
        "active_tab": "backups"
    })

@app.post("/backups/create")
async def create_backup():
    # در آینده اسکریپت بکاپ را فراخوانی می‌کنیم
    return RedirectResponse("/backups?created=1", status_code=303)

# ====================== Run ======================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
