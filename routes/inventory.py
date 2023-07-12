from fastapi import APIRouter, Depends
from models.inventory import createinventory, GetInventory
from utils.database import get_db
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import Annotated
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import asyncio
from utils.validate_token import validate_token
from utils.exceptions import NotFoundRecord

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)


@router.post("",dependencies=[Depends(validate_token)])
# la funcion va a recibir el modelo importado arriba la primera es la variable
# la variable database depende de esta funcion, antes de entrar a la funcion ejecuta el get_db el annotated es para decir el tipo de dato
#                                                                             esta funcion va a devolver este tipo de dato asynIomotor... y se lo va asignar a database
async def post_inventory(
    crear_inventario: createinventory,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    # traemos la base de datos a la funcion
    #devolvemos el id de esta manera
    inserted_id= await database.inventory.insert_one(
        {
            "_id": str(ObjectId()),
            "name": crear_inventario.name,
            "category": crear_inventario.category,
            "quantify": crear_inventario.quantify,
            "price": crear_inventario.price,
        }
    )
    return JSONResponse(
        content={"created_inventory": inserted_id.inserted_id},
        status_code=201
    )
    

#de esta forma traemos 
#con esto podemos validar varias funciones no necesariamente tiene que ser una
@router.get("", response_model=list[GetInventory],dependencies=[Depends(validate_token)])
async def list_inventory(database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    inventory_list = [inventory async for inventory in database.inventory.find({})]
    return JSONResponse(
        content=jsonable_encoder(inventory_list),
        status_code=200
    )






#para traer solo un item del inventario
@router.get("/{inventory_id}")
#agregamos el parametro para por medio del id buscarlo
async def Get_inventory(
    inventory_id:str,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],):
    
    
    inventory= await database.inventory.find_one(
        {
            "_id": inventory_id,
            
           
        }
    )
    #seria como para buscar un item y sino existe el item devuelvo que no existe
    if not inventory:
        raise NotFoundRecord(f"inventarion con este {inventory_id} no existe")

    return JSONResponse(
        content=inventory,
        status_code=200
    )

#usamos los jsonresponse para ser consistentes a la hora de programar