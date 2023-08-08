from fastapi import FastAPI

app = FastAPI()

# default docs:
# swagger http://127.0.0.1:8000/docs
# redoc http://127.0.0.1:8000/redoc
# uvicorn main:app --reload
# curl http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World -- by FastAPI!"}
