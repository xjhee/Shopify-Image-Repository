from sqlite3.dbapi2 import TimestampFromTicks
import sqlite3
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from app.database.database import DatabaseMethods
from typing import List


app = FastAPI()
app.mount("/app/static", StaticFiles(directory="app/static"), name="static")
app.mount("/app", StaticFiles(directory="app"), name="static")


templates = Jinja2Templates(directory = "app/templates")
templates_home = Jinja2Templates(directory = "app/templates/homepage")
templates_form = Jinja2Templates(directory = "app/templates/add")
templates_search = Jinja2Templates(directory = "app/templates/search")


""" Homepage """
@app.get("/")
def home(request: Request):
    return templates_home.TemplateResponse("home.html", context = {"request": request})



""" Methods to search database"""
@app.get("/search")
def search(request: Request):
    return templates_search.TemplateResponse("form.html", context = {'request': request})



@app.post("/search")
def search_(request: Request, name: str = Form(...)):
    products = DatabaseMethods().search_products(name)
    return templates_search.TemplateResponse("products.html", context = {'request': request, "products": products})



""" Methods to add to database"""
@app.get("/add", response_class = HTMLResponse)
def add(request: Request):
    return templates_form.TemplateResponse("form.html", context = {"request": request})



@app.post("/add")
async def add_(request: Request, 
                        id: int = Form(...), 
                        name: str = Form(...), 
                        price: int = Form(...), 
                        stock: int = Form(...), 
                        file: UploadFile = File(...)):
    try:
        photo_contents = await file.read()
        DatabaseMethods().insert_blob(id, name, photo_contents, price, stock)
        return templates_form.TemplateResponse("form.html", context = {"request": request, "message": "Added product"})

    except sqlite3.Error as error:
        return templates.TemplateResponse("message.html", context = {"request": request, "message": "Failed to add product"})




""" Method to purchase """
@app.get("/purchase")
def show_products(request: Request):
    products = DatabaseMethods().show_tables()
    spent = DatabaseMethods().display_sales()
    return templates.TemplateResponse("products.html", context = {'request': request, "products": products, "spent": spent})



@app.get("/purchase/{product_id}")
def purchase_product(request: Request, product_id):
    if not product_id:
        return templates.TemplateResponse("message.html", context = {"request": request, "message": "Invalid product id"})

    purchase_message = DatabaseMethods().purchase_products(product_id)
    return templates.TemplateResponse("message.html", context = {"request": request, "message": purchase_message})







