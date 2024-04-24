#!/usr/bin/env python3
"""
DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database
        
        Args:
            email (str): User's email
            hashed_password (str): User's hashed password
        
        Returns:
            User: User object added to the database
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by given attributes
        
        Args:
            **kwargs: Arbitrary keyword arguments
        
        Returns:
            User: First user found matching the criteria
        
        Raises:
            NoResultFound: If no user is found
            InvalidRequestError: If wrong query arguments are passed
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes
        
        Args:
            user_id (int): User's ID
            **kwargs: Arbitrary keyword arguments to update
        
        Raises:
            ValueError: If an argument does not correspond to a user attribute
        """
        user = self.find_user_by(id=user_id)
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError(f"Invalid attribute: {key}")
        
        self._session.commit()
