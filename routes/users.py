from fastapi import APIRouter, Depends
from models.users import createusers, Getusers
from utils.database import get_db
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import Annotated
from fastapi.responses import JSONResponse

import asyncio
import secrets
from utils.exceptions import DuplicateRecord

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("")
# la funcion va a recibir el modelo importado arriba la primera es la variable
# la variable database depende de esta funcion, antes de entrar a la funcion ejecuta el get_db el annotated es para decir el tipo de dato
#                                                                             esta funcion va a devolver este tipo de dato asynIomotor... y se lo va asignar a database
async def post_users(
    crear_users: createusers,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    #condicionamos para ver si el usuario que metio el usuario ya existe
    user_exist= await database.users.find_one({
        "email":crear_users.email
    })
    if user_exist:
        raise DuplicateRecord(f"este usuario con este email {crear_users.email} ya existe") 
    # traemos la base de datos a la funcion
    #devolvemos el id de esta manera
    inserted_id= await database.users.insert_one(
        {
            "_id": str(ObjectId()),
            "email": crear_users.email,
            "token":secrets.token_hex(12)
           
        }
    )
    return {"crear_user":inserted_id.inserted_id}

@router.get("/{user_id}")
#agregamos el parametro para por medio del id buscarlo
async def get_user(
    user_id:str,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],):
    
    
    user= await database.users.find_one(
        {
            "_id": user_id,
            
           
        }
    )
    return user