from sqlalchemy.orm import Session

from app.models.website_theme import WebsiteTheme

from app.schemas.website_theme_schema import (
    WebsiteThemeCreate
)


def create_website_theme(
    db: Session,
    payload: WebsiteThemeCreate
):
    theme = WebsiteTheme(
        **payload.model_dump()
    )

    db.add(theme)
    db.commit()
    db.refresh(theme)

    return theme


def get_website_themes(
    db: Session
):
    return db.query(
        WebsiteTheme
    ).all()