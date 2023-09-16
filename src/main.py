from fastapi import APIRouter, Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.requests import Request

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead
from chat.router import router as router_chat
from config import REDIS_HOST, REDIS_PORT
from operations.router import router as router_operation
from pages.router import router as router_pages

app = FastAPI(title="Trading App")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)
app.include_router(router_pages)
app.include_router(router_chat)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


# yield
async def get_async_session():
    print("Receive session")
    session = "my session"
    yield session
    print("Destroy session")


@app.get("/items")
async def get_items(session=Depends(get_async_session)):
    print(session)
    return [{"id": 1}]


# Parameters
def pagination_params(limit: int = 10, skip: int = 0):
    return {"limit": limit, "skip": skip}


@app.get("/subjects")
async def get_subject(pag_params: dict = Depends(pagination_params)):
    return [{"id": 1}]


# Class
class Paginator:
    def __init__(self, limit: int = 10, skip: int = 0):
        self.limit = limit
        self.skip = skip


@app.get("/subjects_class")
async def get_subject_class(pag_params: Paginator = Depends(Paginator)):
    return pag_params


# dependencies = [Depends(...)]
class AuthGuard:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, request: Request):
        if "supper_cookie" not in request.cookies:
            raise HTTPException(status_code=403, detail="Forbidden")

        return True


auth_guard_payments = AuthGuard("payments")


router = APIRouter(dependencies=[Depends(auth_guard_payments)])


# @app.get("/payments", dependencies=[Depends(auth_guard_payments)])
# async def get_payments():
#     return "my payments"


@app.get("/payments")
async def get_payments():
    return "my payments"
