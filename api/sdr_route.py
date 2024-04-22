from fastapi.routing import APIRouter
from config.auth import verified_user, authorize, pwd_context, create_access_jwt, create_refresh_token
from schemas.user import User, UserGet, UserPost, UserLogin
from fastapi import Depends, status, HTTPException

sdr_router = APIRouter(prefix='/api/v1', tags=['SDR Test'])

@sdr_router.get('/sdr_test')
async def refresh(token_data:dict = Depends(verified_user)):
    return "sdr user terminal test"
