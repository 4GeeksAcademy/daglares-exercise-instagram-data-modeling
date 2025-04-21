
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from eralchemy2 import render_er
from typing import List

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=True)
    username: Mapped[str] = mapped_column(nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)

    followers: Mapped[List["Follower"]] = relationship(
        foreign_keys=["Follower.user_from_id"])
    following: Mapped[List["Follower"]] = relationship(
        foreign_keys=["Follower.user_to_id"])
    
class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship()

class Media(Base):
    __tablename__ = "media"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=True)
    true: Mapped[str] = mapped_column(nullable=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    
    post: Mapped["Post"] = relationship()

class Comment(Base):
    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str]=mapped_column(nullable=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    author: Mapped["User"] = relationship()
    post: Mapped["Post"] = relationship()

class Follower(Base):
    __tablename__ = "follower"
    id: Mapped[int] = mapped_column(primary_key=True)

    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
