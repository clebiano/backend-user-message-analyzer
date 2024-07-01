import re
import subprocess

from typing import Optional
from pathlib import Path
from fastapi import status, HTTPException

from app.user.schemas import UserOut, UserCollectionOut

BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIRECTORY = BASE_DIR / "tmp"
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)


class UserService:
    async def check_if_file_exists(self, filename: str) -> bool:
        file_path = UPLOAD_DIRECTORY / filename
        file_exists = file_path.is_file() # por que não exists()?

        if not file_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The specified file does not exist")

        return file_exists

    async def get_users(self, order: str, limit: int, offset: int, username: Optional[str], file_name: str) -> UserCollectionOut:
        await self.check_if_file_exists(filename=file_name)

        file_path = UPLOAD_DIRECTORY / file_name

        command = ["./scripts/order-by-username.sh", file_path, f"-{order}"]
        shell_result = subprocess.run(command, capture_output=True, text=True)

        if shell_result.returncode != 0:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error executing the sorting script")

        users = self.parse_users(shell_result.stdout)
        
        if username:
            users = [user for user in users if username.lower() in user['username'].lower()]

        start = offset
        end = start + limit
        paginated_users = users[start:end]

        return UserCollectionOut(
            meta={
                "page": {
                    "limit": limit,
                    "offset": offset,
                    "count": len(paginated_users)
                }
            },
            results=paginated_users
        )

    def parse_users(self, input: str):
        users = []

        for line in input.splitlines():
            parts = re.split(r'\s+', line)
            username = parts[0]
            folder = parts[1]
            number_messages = int(parts[2])
            size = int(parts[4])

            users.append({
                "username": username,
                "folder": folder,
                "numberMessages": number_messages,
                "size": size
            })

        return users

    async def get_users_by_inbox_count(self, event) -> UserCollectionOut:
        return UserCollectionOut()

    async def get_user_by_message_size(self, event) -> UserOut:
        return UserOut()
