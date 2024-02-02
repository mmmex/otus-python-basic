from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/ping/")
def ping():
    return {"message": "pong"}