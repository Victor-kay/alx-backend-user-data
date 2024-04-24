#!/usr/bin/env python3
"""
Module defining User model for the users table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User class representing the users table in the database.
    """
    __tablename__ = 'users'
    
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)
