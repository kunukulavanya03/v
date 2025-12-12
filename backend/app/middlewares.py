from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models import User
from app.utils import get_user_from_token

auth_middleware = Depends(get_user_from_token)

async def get_user_from_token(token: str):
    user = User.query.filter_by(token=token).first()
    if user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    return user