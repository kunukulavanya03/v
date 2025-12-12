from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models import User, Item
from app.middlewares import auth_middleware

user_routes = APIRouter(prefix='/users')
item_routes = APIRouter(prefix='/items')

@user_routes.get('/{id}')
def get_user(id: int):
    user = User.query.get(id)
    return user

@item_routes.post('/')
def create_item(item: Item):
    db.session.add(item)
    db.session.commit()
    return item

@item_routes.get('/')
def get_items():
    items = Item.query.all()
    return items

@item_routes.put('/{id}')
def update_item(id: int, item: Item):
    db_item = Item.query.get(id)
    db_item.title = item.title
    db_item.description = item.description
    db.session.commit()
    return db_item

@item_routes.delete('/{id}')
def delete_item(id: int):
    db_item = Item.query.get(id)
    db.session.delete(db_item)
    db.session.commit()
    return {'message': 'Item deleted successfully'}