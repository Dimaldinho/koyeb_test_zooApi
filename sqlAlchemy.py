from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import json

def load_config(filename):
    with open(filename, 'r') as f:
        config = json.load(f)
    return config


config = load_config('config.json')
dbFile = config["dbname"]


# Change the connection string to point to a SQLite file in the 'db' folder
engine = create_engine(dbFile, echo=True)

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
