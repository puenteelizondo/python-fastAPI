from utils.database import get_db
from typing import Annotated
from fastapi import Header
from utils.exceptions import Unauthorized

async def validate_token(x_token:Annotated[str,Header()]):
    database=await get_db()
    token_exist= await database.users.find_one({"token":x_token})
    #imprimimos para empezar a validar en las funciones
    #print(token_exist)
    if not token_exist:
        raise Unauthorized("token invalido")

    else:
        print("autorizado")

    return True