from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base, User, Item
from schemas import UserCreate, UserResponse, ItemCreate, ItemResponse
import logging

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="V_Is_A_Web_Application_That_Provides_A_Platform_For_Users_To_Manage_Their_Data._The_Backend_Api_Is_Built_Using_Fastapi_And_Sqlalchemy,_And_It_Provides_A_Restful_Interface_For_The_React_Frontend_To_Interact_With. API",
    description="Complete backend API",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to V_Is_A_Web_Application_That_Provides_A_Platform_For_Users_To_Manage_Their_Data._The_Backend_Api_Is_Built_Using_Fastapi_And_Sqlalchemy,_And_It_Provides_A_Restful_Interface_For_The_React_Frontend_To_Interact_With. API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "v_is_a_web_application_that_provides_a_platform_for_users_to_manage_their_data._the_backend_api_is_built_using_fastapi_and_sqlalchemy,_and_it_provides_a_restful_interface_for_the_react_frontend_to_interact_with."}

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)