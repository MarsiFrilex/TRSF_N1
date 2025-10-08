from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)