from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(UUID, primary_key=True)
    email = Column(String)
    password = Column(String)
    phone = Column(String)

    @classmethod
    def get_fields(self):
        return [col for col in self.__table__.columns.keys() if col is not 'user_id']

    