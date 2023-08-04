from fastapi import FastAPI

app = FastAPI()


# uvicorn main:app --reload
# curl http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World -- by FastAPI!"}
