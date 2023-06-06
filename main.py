from fastapi import FastAPI
import uvicorn

from get_data import get_live_price
app = FastAPI()

@app.get("/")
def home():
    return {"message":"API running..."}

@app.post("/get_price")
def user(symbol:str):
    return get_live_price(symbol)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)