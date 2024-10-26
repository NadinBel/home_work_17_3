from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get('/')
async def start_message():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)