from fastapi.routing import APIRouter
from config.auth import verified_user, authorize, pwd_context, create_access_jwt, create_refresh_token
from schemas.user import User, UserGet, UserPost, UserLogin
from fastapi import Depends, status, HTTPException

hub_router = APIRouter(prefix='/api/v1', tags=['Hub Capacity'])

@hub_router.get('/hub_capacity')
async def refresh(token_data:dict = Depends(verified_user)):
    return "hub capacity"

# @auth_router.get('/data')
# async def protected_data(user:dict = Depends(verified_user)):
#     return user 
# {'status':'Authorized',
#             'email':user.email}