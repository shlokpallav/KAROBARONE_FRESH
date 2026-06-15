from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.controllers.website_theme_controller import (
    create_website_theme,
    get_website_themes
)

from app.schemas.website_theme_schema import (
    WebsiteThemeCreate
)

router = APIRouter(
    prefix="/website-themes",
    tags=["Website Themes"]
)


@router.post("/")
def create_website_theme_route(
    payload: WebsiteThemeCreate,
    db: Session = Depends(get_db)
):
    return create_website_theme(
        db,
        payload
    )


@router.get("/")
def get_website_themes_route(
    db: Session = Depends(get_db)
):
    return get_website_themes(db)