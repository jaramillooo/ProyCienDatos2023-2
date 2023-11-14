import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/")
def root():
    return {'message': 'Hello World!'}


@app.get("/item/{item_id}")
def read_item(item_id):
    return {'item id': item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=False)