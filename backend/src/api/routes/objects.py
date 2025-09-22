from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/objects",
    tags=["Objects"],
)