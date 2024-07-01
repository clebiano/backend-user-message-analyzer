import re

from pathlib import Path
from fastapi import UploadFile, status, HTTPException

from app.file.schemas import FileOut, FileCollectionOut

BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIRECTORY = BASE_DIR / "tmp"
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)


class FileService:
    async def check_if_file_exists(self, filename: str) -> bool:
        file_path = UPLOAD_DIRECTORY / filename
        file_exists = file_path.is_file()

        return file_exists

    async def save_file(self, file: UploadFile) -> FileOut:
        if not re.match(r'^[\w\-.]+$', file.filename):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file name. Allowed characters: A-Z, a-z, 0-9, -, _"
            )

        file_path = UPLOAD_DIRECTORY / file.filename

        with file_path.open("wb") as f:
            f.write(await file.read())

        return FileOut(file_name=file.filename, size=file_path.stat().st_size)

    async def get_files(self) -> FileCollectionOut:
        files = []

        for file_path in list(UPLOAD_DIRECTORY.glob("**/*")):
            if file_path.is_file():
                file_info = {
                    "file_name": file_path.name,
                    "size": file_path.stat().st_size
                }
                files.append(file_info)

        return FileCollectionOut(results=files)
