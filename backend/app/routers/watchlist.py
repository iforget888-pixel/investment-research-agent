from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import WatchlistItem
from app.schemas import WatchlistItemCreate, WatchlistItemRead, WatchlistItemUpdate

router = APIRouter()


@router.get("", response_model=list[WatchlistItemRead])
def list_watchlist_items(session: Session = Depends(get_session)) -> list[WatchlistItem]:
    return list(session.scalars(select(WatchlistItem).order_by(WatchlistItem.created_at.desc())))


@router.post("", response_model=WatchlistItemRead, status_code=status.HTTP_201_CREATED)
def create_watchlist_item(payload: WatchlistItemCreate, session: Session = Depends(get_session)) -> WatchlistItem:
    item = WatchlistItem(**payload.model_dump())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/{item_id}", response_model=WatchlistItemRead)
def get_watchlist_item(item_id: UUID, session: Session = Depends(get_session)) -> WatchlistItem:
    item = session.get(WatchlistItem, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Watchlist item not found")
    return item


@router.patch("/{item_id}", response_model=WatchlistItemRead)
def update_watchlist_item(
    item_id: UUID,
    payload: WatchlistItemUpdate,
    session: Session = Depends(get_session),
) -> WatchlistItem:
    item = session.get(WatchlistItem, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Watchlist item not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    session.commit()
    session.refresh(item)
    return item
