from fastapi import APIRouter, Depends, status

from app.user.services import UserService
from app.user.schemas import UserOut, UserCollectionOut

router = APIRouter()


@router.get(
    '',
    summary='List users in either ascending or descending order',
    status_code=status.HTTP_200_OK,
    response_model=UserCollectionOut,
)
async def ge(
    service: UserService = Depends(),
) -> UserCollectionOut:
    users = await service.get_users()

    return users


@router.get(
    '/filter-by-inbox-count',
    summary='Filter users based on the number of messages in their inbox',
    status_code=status.HTTP_200_OK,
    response_model=UserCollectionOut,
)
async def get(
    service: UserService = Depends(),
) -> UserCollectionOut:
    users = await service.get_users_by_inbox_count()

    return users


@router.get(
    '/filter-by-message-size',
    summary='Filter the user with the largest or smallest message size',
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
)
async def get(
    service: UserService = Depends(),
) -> UserOut:
    user = await service.get_user_by_message_size()

    return user
