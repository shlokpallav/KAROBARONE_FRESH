from fastapi import FastAPI
from app.routes import store_routes
from app.database import Base, engine
from app.models.store import Store
from app.routes import social_platform_routes
from app.routes import social_links_routes
from app.routes import store_business_hours_routes
from app.routes import store_branding_routes
from app.routes import store_bank_account_routes
from app.routes import sections_routes
from app.routes import seo_metadata_routes
from app.routes import media_metadata_routes
from app.routes import website_theme_routes

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello"}
app.include_router(store_routes.router)
app.include_router(
    social_platform_routes.router
)
app.include_router(
    social_links_routes.router
)
app.include_router(
    store_business_hours_routes.router
)
app.include_router(
    store_branding_routes.router
)
app.include_router(
    store_bank_account_routes.router
)
app.include_router(
    sections_routes.router
)
app.include_router(
    seo_metadata_routes.router
)
app.include_router(
    media_metadata_routes.router
)
app.include_router(
    website_theme_routes.router
)