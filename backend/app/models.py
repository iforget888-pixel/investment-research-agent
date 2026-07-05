import uuid
from datetime import date, datetime
from typing import Literal

from sqlalchemy import Date, DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

WatchlistStatus = Literal["active", "paused", "archived"]
AssetType = Literal["public_equity", "private_company", "theme", "industry"]
MaterialType = Literal["url", "note", "pdf", "image", "filing", "transcript"]
MaterialStatus = Literal["new", "processed", "archived"]


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class WatchlistItem(TimestampMixin, Base):
    __tablename__ = "watchlist_items"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(180), nullable=False)
    asset_type: Mapped[str] = mapped_column(String(40), nullable=False, default="public_equity")
    ticker: Mapped[str | None] = mapped_column(String(32), nullable=True)
    exchange: Mapped[str | None] = mapped_column(String(32), nullable=True)
    industry: Mapped[str | None] = mapped_column(String(120), nullable=True)
    theme: Mapped[str | None] = mapped_column(String(120), nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="active")
    thesis: Mapped[str | None] = mapped_column(Text, nullable=True)
    key_metrics: Mapped[list[str]] = mapped_column(JSONB, nullable=False, default=list)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    raw_materials: Mapped[list["RawMaterial"]] = relationship(back_populates="watchlist_item")


class RawMaterial(TimestampMixin, Base):
    __tablename__ = "raw_materials"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    watchlist_item_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("watchlist_items.id", ondelete="SET NULL"),
        nullable=True,
    )
    material_type: Mapped[str] = mapped_column(String(40), nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    source_name: Mapped[str | None] = mapped_column(String(180), nullable=True)
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    content_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    published_at: Mapped[date | None] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="new")
    metadata_json: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)

    watchlist_item: Mapped[WatchlistItem | None] = relationship(back_populates="raw_materials")
