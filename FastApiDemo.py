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


