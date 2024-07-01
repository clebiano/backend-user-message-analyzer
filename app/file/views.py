from fastapi import APIRouter, Depends, status, UploadFile, Response, Query

from app.file.schemas import FileOut, FileCollectionOut
from app.file.services import FileService

router = APIRouter()


@router.put(
    '',
    summary='Upload files',
    status_code=status.HTTP_201_CREATED,
    response_model=FileOut,
)
async def put(
    file: UploadFile,
    response: Response,
    service: FileService = Depends(),
) -> FileOut:
    file_exists = await service.check_if_file_exists(filename=file.filename)

    if file_exists:
        response.status_code = status.HTTP_204_NO_CONTENT

    file = await service.save_file(file)

    return file


@router.get(
    '',
    summary='List uploaded files',
    status_code=status.HTTP_200_OK,
    response_model=FileCollectionOut,
)
async def get(
    limit: int = Query(10, ge=1, description="Limit the number of files returned"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
    # file_name: str = Query(..., description="File to be processed"),
    service: FileService = Depends(),
) -> FileCollectionOut:
    files = await service.get_files(limit=limit, offset=offset)

    return files
