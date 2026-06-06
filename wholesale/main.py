from fastapi import FastAPI

from apis import client_api
from apis import location_api
from apis import product_api
from apis import sale_api

app = FastAPI(
    title="Wholesale System",
    description="API Service",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(client_api.router)
app.include_router(location_api.router)
app.include_router(product_api.router)
app.include_router(sale_api.router)
