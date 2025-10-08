from services.s3_service import S3Service
from src.repositories.auth_repository import AuthRepository
from src.repositories.defects_repository import DefectsRepository
from src.repositories.objects_repository import ObjectsRepository
from src.repositories.roles_repository import RolesRepository
from src.repositories.statuses_repository import StatusesRepository
from src.repositories.tags_repository import TagsRepository
from src.repositories.users_repository import UsersRepository

from src.services.auth_service import AuthService
from src.services.defects_service import DefectsService
from src.services.objects_service import ObjectsService
from src.services.roles_service import RolesService
from src.services.statuses_service import StatusesService
from src.services.tags_service import TagsService


async def get_auth_service() -> AuthService:
    return AuthService(AuthRepository(), UsersRepository())


async def get_defects_service() -> DefectsService:
    return DefectsService(DefectsRepository())


async def get_objects_service() -> ObjectsService:
    return ObjectsService(ObjectsRepository())


async def get_roles_service() -> RolesService:
    return RolesService(RolesRepository())


async def get_tags_service() -> TagsService:
    return TagsService(TagsRepository())


async def get_statuses_service() -> StatusesService:
    return StatusesService(StatusesRepository())


async def get_s3_service() -> S3Service:
    return S3Service()