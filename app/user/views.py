from typing import Optional
from fastapi import APIRouter, Depends, status, Query

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
    order: str = Query("asc", regex="^(asc|desc)$", description="Order by ascending or descending"),
    limit: int = Query(10, ge=1, description="Limit the number of users returned"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
    username: Optional[str] = Query(None, description="Filter by username"),
    file_name: str = Query(..., description="File to be processed"),
    service: UserService = Depends(),
) -> UserCollectionOut:
    users = await service.get_users(order=order, limit=limit, offset=offset, username=username, file_name=file_name)

    return users


@router.get(
    '/filter-by-inbox-count',
    summary='Filter users based on the number of messages in their inbox',
    status_code=status.HTTP_200_OK,
    response_model=UserCollectionOut,
)
async def get(
    limit: int = Query(10, ge=1, description="Limit the number of users returned"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
    username: Optional[str] = Query(None, description="Filter by username"),
    file_name: str = Query(..., description="File to be processed"),
    min_msgs: int = Query(0, ge=0, description="Specifies the minimum number of messages in the user's inbox"),
    max_msgs: int = Query(100, ge=1, description="Specifies the maximum number of messages in the user's inbox"),
    service: UserService = Depends(),
) -> UserCollectionOut:
    users = await service.get_users_by_inbox_count(
        limit=limit, offset=offset, username=username, file_name=file_name, min_msgs=min_msgs, max_msgs=max_msgs
    )

    return users


@router.get(
    '/filter-by-message-size',
    summary='Filter the user with the largest or smallest message size',
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
)
async def get(
    selection_criteria: str = Query(..., regex="^(min|max)$", description="Specifies the selection criteria based on "
                                    "message size: 'min' to select the user with the smallest total message size, "
                                    "'max' to select the user with the largest total message size."),
    file_name: str = Query(..., description="File to be processed"),
    service: UserService = Depends(),
) -> UserOut:
    user = await service.get_user_by_message_size(selection_criteria=selection_criteria, file_name=file_name)

    return user
