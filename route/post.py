from fastapi import APIRouter
from model.post import Post 
from config.db import conn 
from schemas.post import  serializeList
user = APIRouter() 

@user.get('/')
async def find_all_users():
    return serializeList(conn.Job.camp.find())