from fastapi import FastAPI, HTTPException, Request # type: ignore

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id % 2==0:
        return {f"item_id {item_id} is even"}
    else:
        return {f"item_id {item_id} is odd"}
    
@app.post("/users/")
async def create_user(request: Request): 
    user_data = await request.json()
    if not user_data:
        raise HTTPException(
            status_code=400,
            detail="User data must be provided"
        )
    return {"user": user_data}


# from typing import Dict
# from functools import wraps
# import logging

# logging.basicConfig(level=logging.WARNING)

# def validate_item_id(func):
#     @wraps(func)
#     async def wrapper(item_id: int) -> Dict[str,str]:
#         if item_id is None:
#             logging.warning("Item ID is None")
#             raise HTTPException(status_code=400, detail="number must be provisioned")

#         result = await func(item_id)
#         return result    
   
#     return wrapper

# @validate_item_id


# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     match item_id:
#         case item_id if item_id % 2==0:
#             return {f"item_id {item_id} is even"}
#             #raise HTTPException(status_code=418, detail="Item is odd")
#         case item_id if item_id % 2==1:
#             return {f"item_id {item_id} is odd"}
#             #raise HTTPException(status_code=418, detail="Item is odd")        
#         case _:
#             raise HTTPException(status_code=400, detail="number must be provided")

    # case item_id if not item_id.isdigit:
    #     raise HTTPException(status_code=418, detail="not a number")   
    # if item_id != "":
    #     if item_id % 2 == 0:
    #         return {f"item_id {item_id} is even"}
    #     else:
    #         return {f"item_id {item_id} is odd"}
    # else:
    #     raise HTTPException(status_code=400, detail="number must be provided")    



# http://127.0.0.1:8000/items/2
#   detail	"Item is odd"
# http://127.0.0.1:8000/items/1
#   item_id	1

# curl -X POST http://127.0.0.1:8000/users/ -H "Content-Type: application/json" -d '{"name": "Joakime", "age": 47}'
# response: {"user":{"name":"Joakime","age":47}}


# Server
# Starta Server: 'fastapi dev main.py'
# Stoppa server: 'ctrc-c'

# Server started at http://127.0.0.1:8000
# Documentation at http://127.0.0.1:8000/docs

# Venv
# 'activate' för att starta
# 'deactivate' för att stoppa

# https://reqbin.com/req/c-1n4ljxb9/curl-get-request-example
# curl GET http://127.0.0.1:8000  


# https://code.visualstudio.com/docs/python/environments
# https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments


# Uvicorn is an ASGI web server implementation for Python. https://www.uvicorn.org/
# $ pip install 'uvicorn[standard]'


# uvicorn(WSGI server)
# pydantic kontrollerar indata (validator)
# https://medium.com/@marcnealer/a-practical-guide-to-using-pydantic-8aafa7feebf6