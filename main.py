from fastapi import FastAPI
from app.api.v1.cliente_controller import router

app = FastAPI()

@app.get('/',response_model=None)
async def hello()->dict:
    return {"message": "Hello World"}

app.include_router(router)
