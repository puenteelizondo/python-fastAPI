
#para importar la libreria
from fastapi import FastAPI
#para abrirlas
app= FastAPI()

#hacer endpoints
#app es para hacer endpoint y si quieres otros metodos solo cambias el .delete o asi
@app.get("/Holaa brooooo")
#usamos funciones async porque esta api puede hacer muchas funciones a la vez
#django solo podia hacer una funcion a la vez por eso era sincrono
#siempre que hagamos una funcion asincrona tenemos que usar el async
async def healcheck():
    return {
        "healcheck":"Saludooos se bañan"
    }

