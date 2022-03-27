from typing import Optional
from uuid import uuid4

from sqlmodel import Field, SQLModel


class Auditable(SQLModel):
    created_at: Optional[str] = Field(
        description="The resource creation timestamp", default=None
    )
    modified_at: Optional[str] = Field(
        description="The resource last modification timestamp", default=None
    )
    created_by: Optional[str] = Field(
        description="The user who created the resource", default=None
    )
    modified_by: Optional[str] = Field(
        description="The user who last modified the resource", default=None
    )
    deleted: bool = Field(
        default=False, description="Whether resource has been deleted"
    )
    deleted_at: Optional[str] = Field(
        description="Timestamp when the resource was deleted", default=None
    )
    deleted_by: Optional[str] = Field(
        description="User ID who deleted the resource", default=None
    )


class ResourceTable(Auditable):
    id: Optional[str] = Field(
        default_factory=lambda: str(uuid4()),
        primary_key=True,
    )


class ResourceTableDBResponse(SQLModel):
    id: str
    created_at: Optional[str] = Field(
        description="The resource creation timestamp", default=None
    )
    modified_at: Optional[str] = Field(
        description="The resource last modification timestamp", default=None
    )
    created_by: Optional[str] = Field(
        description="The user who created the resource", default=None
    )
    modified_by: Optional[str] = Field(
        description="The user who last modified the resource", default=None
    )
