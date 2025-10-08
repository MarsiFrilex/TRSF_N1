from fastapi import APIRouter

from src.api.routes.accounts_router import router as accounts_router
from src.api.routes.defects_router import router as defects_router
from src.api.routes.objects_router import router as objects_router
from src.api.routes.auth_router import router as auth_router
from src.api.routes.roles_router import router as roles_router
from src.api.routes.tags_router import router as tags_router
from src.api.routes.statuses_router import router as statuses_router
from src.api.routes.cloud_router import router as cloud_router

base_router = APIRouter()
base_router.include_router(accounts_router)
base_router.include_router(auth_router)
base_router.include_router(defects_router)
base_router.include_router(objects_router)
base_router.include_router(roles_router)
base_router.include_router(tags_router)
base_router.include_router(statuses_router)
base_router.include_router(cloud_router)