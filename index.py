from fastapi import FastAPI
from route.post import user 
app = FastAPI()
app.include_router(user)