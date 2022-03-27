from typing import List, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def configure_cors(
    app: FastAPI,
    allow_origins: Optional[List[str]] = ["*"],
    allow_credentials: Optional[bool] = True,
    allow_methods: Optional[List[str]] = ["*"],
    allow_headers: Optional[List[str]] = ["*"],
) -> None:
    """Configure CORS middleware

    Args:
        app (FastAPI): [description]
        allow_origins (Optional[List[str]], optional): List of origins. Defaults to ["*"].
        allow_credentials (Optional[bool], optional): Whether to allow credentials. Defaults to True.
        allow_methods (Optional[List[str]], optional): List of methods. Defaults to ["*"].
        allow_headers (Optional[List[str]], optional): List of headers. Defaults to ["*"].
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # all origins
        allow_credentials=True,
        allow_methods=["*"],  # all methods
        allow_headers=["*"],  # all headers
    )
