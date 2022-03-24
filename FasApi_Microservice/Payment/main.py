from fastapi import FastAPI
from redis import Redis
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from starlette.requests import Request
import requests
import time

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

class Order(HashModel):
    product_id: str
    price: float
    fee = float
    total: float
    quantity: int
    status: str
    
    class Meta:
        database = redis

def order_completed(order:Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()
    redis.xadd('order_completed', order.dict(), '*')

@app.post('/orders')
async def create_order(request:Request, background_task: BackgroundTasks):
    body = await request.json()
    req = requests.get('http://127.0.0.1:8000/products/%s' % body['id'])
    product = req.json()
    order = Order(
        product_id = body['id'],
        price = product['price'],
        fee = 0.2*product['price'],
        total = 1.2*product['price'],
        quantity = body['quantity'],
        status = 'pending'
    )
    order.save()
    background_task.add_task(order_completed, order)
    return order
    
@app.get('/orders/{pk}')
def get_order(pk:str):
    order = Order.get(pk)
    redis.xadd('refund_order', order.dict(), '*')
    return order