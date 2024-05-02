from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Change the connection string to point to a SQLite file in the 'db' folder
engine = create_engine('sqlite:///zoo.db', echo=True)

# Declare a base class for declarative class definitions
Base = declarative_base()
Base.metadata.create_all(engine)

# Define a class representing a User table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"
    
# Create the database schema
