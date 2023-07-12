# esta libreria es para validar modelos aqui
from pydantic import BaseModel

# asi se crean las tablas


class createinventory(BaseModel):
    name: str
    category: str
    quantify: str
    price: float

#es para hacer el get del inventario
class GetInventory(BaseModel):
    #el _ es para una propiedad pribada 
    _id: str
    name: str
    category: str
    quantify: str
    price : float
