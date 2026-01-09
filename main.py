from fastapi import FastAPI
from app.api.v1.cliente_controller import router as cliente_router
from app.api.v1.usuario_controller import router as usuario_router
from app.api.v1.envio_controller import router as envio_router
from app.api.v1.seguimiento_controller import router as seguimiento_router

app = FastAPI()


@app.get('/', response_model=None)
async def hello() -> dict:
    return {"message": "Hello World"}


app.include_router(cliente_router)
app.include_router(usuario_router)
app.include_router(envio_router)
app.include_router(seguimiento_router)
