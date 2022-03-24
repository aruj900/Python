from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ['http://127.0.0.1:3000'],
    allow_methods= ['*'],
    allow_headers= ['*']
)

redis = get_redis_connection(
    host = "redis-19699.c264.ap-south-1-1.ec2.cloud.redislabs.com",
    port = 19699,
    password = "lWNYAKsQQdiBhuPGFgZ2uEnqOdEKFeJf",
    decode_responses= True
)

class Product(HashModel):
    name: str
    price: int
    quantity: int
    
    class Meta:
        database = redis

def format(pk:str):
    product = Product.get(pk)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }

@app.get("/products")
def product():
    return [format(pk) for pk in Product.all_pks()]

@app.post("/products")
def create(product: Product):
    return product.save()

@app.get('/products/{pk}')
def get_product(pk:str):
    return Product.get(pk)

@app.delete('/products/{pk}')
def delete_product(pk:str):
    return Product.delete(pk)
