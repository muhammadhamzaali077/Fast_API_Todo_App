from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel


app = FastAPI(title="Hello World API", 
    version="0.0.1",
    servers=[
        {
            "url": "http://0.0.0.0:8000",
            "description": "Development Server"
        }
        ])


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None




@app.get("/")
def read_root():
    return {"Hello": "Hamza"}


@app.get("/items/{item_id}")
def read_item(item_id: int, item_query: Union[str, None] = None):
    return {"item_id": item_id, "your_query": item_query}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# from typing import Annotated

# from fastapi import Depends, FastAPI

# app = FastAPI()


# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/items/")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons