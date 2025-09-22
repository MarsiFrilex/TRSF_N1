from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/defects",
    tags=["Defects"],
)