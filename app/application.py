from typing import Any

from fastapi import FastAPI, APIRouter


class Application(FastAPI):
    def __init__(self: 'Application', router: APIRouter, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            title='backend-user-message-analyzer',
            version='0.0.0',
            # responses='respostas comuns',
            *args,
            **kwargs,
        )

        self.include_router(router=router)
