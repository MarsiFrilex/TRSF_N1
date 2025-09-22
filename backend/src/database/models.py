from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func

from src.database.connection import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)


class Defects(Base):
    __tablename__ = "defects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    object_id = Column(Integer, ForeignKey('objects.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
    registrator_id = Column(Integer, ForeignKey('users.id'))
    engineer_id = Column(Integer, ForeignKey('users.id'))
    status_id = Column(Integer, ForeignKey('statuses.id'))
    deadline = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)


class Statuses(Base):
    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)


class Objects(Base):
    __tablename__ = "objects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String, nullable=False)
    description = Column(String, nullable=True)