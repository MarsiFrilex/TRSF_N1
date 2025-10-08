import asyncio

import uvicorn

from fastapi import FastAPI

from src.api.base_router import base_router
from src.database.connection import delete_tables, create_tables

app = FastAPI()
app.include_router(base_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
