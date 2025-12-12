from fastapi import HTTPException
from app.models import User

async def get_user_from_token(token: str):
    user = User.query.filter_by(token=token).first()
    if user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    return user