from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    login = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    user_items = relationship("Item", back_populates='owner', cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user")
    
    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, login={self.login!r}, email={self.email!r})"
    
class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True)
    item_title = Column(String(255), nullable=False)
    item_description = Column(String(255), nullable=False)
    item_cost = Column(Integer, nullable=False)
    item_image = Column(String(300), nullable=False)
    item_owner = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    owner = relationship("User", back_populates="user_items")
    carts = relationship("Cart", back_populates="item")
    
    def __repr__(self) -> str:
        return f"Item(item_id={self.item_id!r}, item_title={self.item_title!r}, item_description={self.item_description!r}, item_owner={self.item_owner!r})"

class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    item_id = Column(Integer, ForeignKey('items.item_id'))
    
    item = relationship("Item", back_populates="carts")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    text = Column(Text, nullable=False)
    rating = Column(Integer)

    # Добавляем связи, чтобы облегчить доступ к связанным объектам (пользователь и товар)
    user = relationship("User", back_populates="reviews")
