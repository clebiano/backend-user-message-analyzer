from fastapi.routing import APIRouter

from app import user, file

router = APIRouter(prefix='/v0')

router.include_router(file.router, prefix="/files", tags=["Files"])
router.include_router(user.router, prefix="/users", tags=["Users"])
