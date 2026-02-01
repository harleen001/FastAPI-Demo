from fastapi import FastAPI
from models import Products

app=FastAPI()

@app.get("/")
def greet():
    return "Welcome to fast api project"

products=[
    Products(1,"phone","budget phone",99,10),
    Products(2,"laptop","gaming laptop",999,6)
]

@app.get("/products")
def get_all_products():
    return "all products"      
