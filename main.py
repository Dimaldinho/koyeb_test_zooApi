from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
import sqlAlchemy as sqlAlc
from sqlalchemy.orm import sessionmaker

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "He\eb"}

@app.get("/get-all-animals")
def getAnimals():
    Session = sessionmaker(bind=sqlAlc.engine)
    session = Session()
    
    animal = session.query(sqlAlc.User).all()
    print(animal)
    
    return animal

@app.get("/get-animal")
def getOneAnimal(animal_name: Optional[str] = None, animal_id: Optional[int]= None):
    Session = sessionmaker(bind=sqlAlc.engine)
    session = Session()
    animal = session.query(sqlAlc.User).all()

    for  i in animal:
        if i.id == animal_id or i.name == animal_name:
            return i
    return {"Data: Not Found"}

@app.post("/create-animal/{id}")
def createAnimal(animal_name : str, animal_age : int):
    Session = sessionmaker(bind=sqlAlc.engine)
    session = Session()
    
    new_animal = sqlAlc.User(name=animal_name, age=animal_age)

    session.add(new_animal)
    session.commit()

@app.put("/update-animal/{animal_id}")
def updateAnimal(animal_id: int, animal_name:str,animal_age: int):
    Session = sessionmaker(bind=sqlAlc.engine)
    session = Session()

    animal = session.query(sqlAlc.User).filter_by(id=animal_id).first()
    
    animal.name = animal_name
    animal.age = animal_age
    session.commit()
    
    


@app.delete("/delete-animal/{animal_id}")
def deleteAnimal(animal_id:int):
    Session = sessionmaker(bind=sqlAlc.engine)
    session = Session()

    animal = session.query(sqlAlc.User).filter_by(id=animal_id).first()
    if animal:
        session.delete(animal)
        session.commit()

