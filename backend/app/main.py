from fastapi import FastAPI
from dotenv import load_dotenv
from app.database import engine
from app.routes import user_routes, item_routes
from app.middlewares import auth_middleware

load_dotenv()
app = FastAPI()
app.include_router(user_routes)
app.include_router(item_routes)
app.add_middleware(auth_middleware)
