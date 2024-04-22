from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from config.settings import Config
from api.auth_route import auth_router
from api.hub_route import hub_router
from api.sdr_route import sdr_router

import uvicorn

app = FastAPI(
    title="API NMS N3 Skeleton",
    description="API for handle SDR Hub Capacity and SDR User Terminal Test",
    version="0.0.1",
    terms_of_service="",
    contact={
        "name": "NMS Team",
    },
    license_info={
        "name": "n",
        "url": "https://n.co.id",
    },
)

for router in [auth_router, hub_router, sdr_router]:
    app.include_router(router)

register_tortoise(
    app,
    db_url=Config.DB_URL,
    add_exception_handlers=True,
    generate_schemas=False,
    modules={'models': Config.DB_MODELS}
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)