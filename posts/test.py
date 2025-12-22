from datetime import datetime
from typing import List
from typing import Optional
from sqlalchemy import DateTime, ForeignKey, create_engine, func, select
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

engine = create_engine("postgresql://postgres:admin@localhost/p51_users_test")


def main():
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        if session.query(User).count() == 0:
            session.add_all(
                [
                    User(name="sandy", fullname="Sandy Cheeks"),
                    User(name="jim", fullname="Jim Jones"),
                    User(name="cathy", fullname="Cathy Carcon"),                    
                ]
            )
            session.commit()
                
        for user in session.scalars(select(User)):
            print(user)       

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    
    posts: Mapped[List["Post"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

class Post(Base):
    __tablename__ = "posts"
    title: Mapped[str] = mapped_column(String(30))
    content: Mapped[str] = mapped_column(String(255))
    
    user: Mapped["User"] = relationship(back_populates="post")
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
 
        
        
class Likes(Base):
    __tablename__ = "liks"
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    post_id: Mapped[str] = mapped_column(ForeignKey("post_account.id"))
   




class Comments(Base):
    __tablename__ = "comments"
    publication_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id")) 
    user: Mapped["User"] = relationship(back_populates="posts") di

