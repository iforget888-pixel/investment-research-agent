from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class WatchlistItemBase(BaseModel):
    name: str = Field(min_length=1, max_length=180)
    asset_type: str = "public_equity"
    ticker: str | None = Field(default=None, max_length=32)
    exchange: str | None = Field(default=None, max_length=32)
    industry: str | None = Field(default=None, max_length=120)
    theme: str | None = Field(default=None, max_length=120)
    status: str = "active"
    thesis: str | None = None
    key_metrics: list[str] = Field(default_factory=list)
    notes: str | None = None


class WatchlistItemCreate(WatchlistItemBase):
    pass


class WatchlistItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=180)
    asset_type: str | None = None
    ticker: str | None = Field(default=None, max_length=32)
    exchange: str | None = Field(default=None, max_length=32)
    industry: str | None = Field(default=None, max_length=120)
    theme: str | None = Field(default=None, max_length=120)
    status: str | None = None
    thesis: str | None = None
    key_metrics: list[str] | None = None
    notes: str | None = None


class WatchlistItemRead(WatchlistItemBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RawMaterialBase(BaseModel):
    watchlist_item_id: UUID | None = None
    material_type: str = "note"
    title: str = Field(min_length=1, max_length=300)
    source_name: str | None = Field(default=None, max_length=180)
    source_url: HttpUrl | None = None
    content_text: str | None = None
    published_at: date | None = None
    status: str = "new"
    metadata_json: dict = Field(default_factory=dict)


class RawMaterialCreate(RawMaterialBase):
    pass


class RawMaterialUpdate(BaseModel):
    watchlist_item_id: UUID | None = None
    material_type: str | None = None
    title: str | None = Field(default=None, min_length=1, max_length=300)
    source_name: str | None = Field(default=None, max_length=180)
    source_url: HttpUrl | None = None
    content_text: str | None = None
    published_at: date | None = None
    status: str | None = None
    metadata_json: dict | None = None


class RawMaterialRead(RawMaterialBase):
    id: UUID
    source_url: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class HealthRead(BaseModel):
    status: str
    service: str
