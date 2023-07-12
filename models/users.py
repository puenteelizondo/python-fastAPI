# esta libreria es para validar modelos aqui
from pydantic import BaseModel

# asi se crean las tablas


class createusers(BaseModel):
   email:str


class Getusers(BaseModel):
    #el _ es para una propiedad pribada 
    _id: str
    email:str