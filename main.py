from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def greet():
    return "Welcome to fast api project"

@app.get("/products")
def get_all_products():
    return "all products"