from app.user.schemas import UserOut, UserCollectionOut


class UserService:
    async def get_users(self, event) -> UserCollectionOut:
        return UserCollectionOut()

    async def get_users_by_inbox_count(self, event) -> UserCollectionOut:
        return UserCollectionOut()

    async def get_user_by_message_size(self, event) -> UserOut:
        return UserOut()
