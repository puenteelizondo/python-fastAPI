# para importar la libreria
from fastapi import FastAPI

# para traer el archivo routs
from routes import inventory,users
#levantamos las excepciones
from utils.exceptions import (
    DuplicateRecord,
    NotFoundRecord,
    Unauthorized,
    Forbidden,
    duplicate_record_exception_handler,
    not_found_exception_handler,
    unauthorized_exception_handler,
    forbidden_exception_handler,
)

# para abrirlas
app = FastAPI()
# con esto lo traigo, osea traer la vista de inventory
app.include_router(inventory.router)
app.include_router(users.router)
#traemos las excepciones 
app.add_exception_handler(DuplicateRecord, duplicate_record_exception_handler)
app.add_exception_handler(NotFoundRecord, not_found_exception_handler)
app.add_exception_handler(Unauthorized, unauthorized_exception_handler)
app.add_exception_handler(Forbidden, forbidden_exception_handler)



# hacer endpoints
# app es para hacer endpoint y si quieres otros metodos solo cambias el .delete o asi
# en vez de default ahora con el tags aparecera healtcheck
# esta vista igual no es necesaria hacerla aqui tendira que ir en routes
@app.get("/healtcheck", tags=["healtcheck"])

# usamos funciones async porque esta api puede hacer muchas funciones a la vez
# django solo podia hacer una funcion a la vez por eso era sincrono
# siempre que hagamos una funcion asincrona tenemos que usar el async
async def healcheck():
    return {"healcheck": "ok"}
