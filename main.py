from fastapi import FastAPI
from models import Products

app=FastAPI()

@app.get("/")
def greet():
    return "Welcome to fast api project"

products=[
    Products(id=1,name="phone", description= "budget phone", price= 99, quantity=10),
    Products(id=2,name="laptop", description= "powerful laptop",price= 999, quantity=30),
    Products(id=3,name="Pen", description= "blue ink pen", price= 9, quantity=100),
]

@app.get("/products")
def get_all_products():
    return products      
