from fastapi import APIRouter

from src.api.routes.accounts import router as accounts_router
from src.api.routes.defects import router as defects_router
from src.api.routes.objects import router as objects_router
from src.api.routes.auth import router as auth_router
from src.api.routes.roles import router as roles_router
from src.api.routes.tags import router as tags_router
from src.api.routes.statuses import router as statuses_router
from src.api.routes.cloud import router as cloud_router

base_router = APIRouter()
base_router.include_router(accounts_router)
base_router.include_router(auth_router)
base_router.include_router(defects_router)
base_router.include_router(objects_router)
base_router.include_router(roles_router)
base_router.include_router(tags_router)
base_router.include_router(statuses_router)
base_router.include_router(cloud_router)