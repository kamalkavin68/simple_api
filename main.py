from fastapi import FastAPI
import uvicorn

from get_data import get_live_price
app = FastAPI()

@app.get("/")
def home():
    return {"message":"API running..."}

@app.get("/user")
def user():
    return {"user": "kavin"}

@app.post("/get_data")
def get_data(symbol:str):
    data = get_live_price(symbol)
    return data

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)