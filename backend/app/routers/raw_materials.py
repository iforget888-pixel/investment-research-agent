from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import RawMaterial, WatchlistItem
from app.schemas import RawMaterialCreate, RawMaterialRead, RawMaterialUpdate

router = APIRouter()


@router.get("", response_model=list[RawMaterialRead])
def list_raw_materials(
    watchlist_item_id: UUID | None = None,
    session: Session = Depends(get_session),
) -> list[RawMaterial]:
    query = select(RawMaterial).order_by(RawMaterial.created_at.desc())
    if watchlist_item_id:
        query = query.where(RawMaterial.watchlist_item_id == watchlist_item_id)
    return list(session.scalars(query))


@router.post("", response_model=RawMaterialRead, status_code=status.HTTP_201_CREATED)
def create_raw_material(payload: RawMaterialCreate, session: Session = Depends(get_session)) -> RawMaterial:
    data = payload.model_dump()
    if payload.source_url:
        data["source_url"] = str(payload.source_url)
    if payload.watchlist_item_id and not session.get(WatchlistItem, payload.watchlist_item_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="watchlist_item_id does not exist")
    material = RawMaterial(**data)
    session.add(material)
    session.commit()
    session.refresh(material)
    return material


@router.get("/{material_id}", response_model=RawMaterialRead)
def get_raw_material(material_id: UUID, session: Session = Depends(get_session)) -> RawMaterial:
    material = session.get(RawMaterial, material_id)
    if not material:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Raw material not found")
    return material


@router.patch("/{material_id}", response_model=RawMaterialRead)
def update_raw_material(
    material_id: UUID,
    payload: RawMaterialUpdate,
    session: Session = Depends(get_session),
) -> RawMaterial:
    material = session.get(RawMaterial, material_id)
    if not material:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Raw material not found")
    data = payload.model_dump(exclude_unset=True)
    if payload.source_url:
        data["source_url"] = str(payload.source_url)
    if data.get("watchlist_item_id") and not session.get(WatchlistItem, data["watchlist_item_id"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="watchlist_item_id does not exist")
    for key, value in data.items():
        setattr(material, key, value)
    session.commit()
    session.refresh(material)
    return material
