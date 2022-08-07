from fastapi import status, HTTPException, Response, Depends, APIRouter

from server import models, schemas, oauth2
from server.database import get_db
from sqlalchemy.orm import Session

from typing import List

router = APIRouter(
    prefix="/exercises",
    tags = ['Work Sessions']
)

@router.get("/", response_model=List[schemas.Exercise])
def get_exercises(db: Session = Depends(get_db)):
    exercises = db.query(models.Exercise).all()
    return exercises

@router.get("/{id}", response_model=schemas.Exercise)
def get_exercise(id: int, db: Session=Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    exercise = db.query(models.Exercise).filter(models.Exercise.id==id).first()

    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Exercise not Found')

    return exercise

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Exercise)
# def create_worksession(workout: schemas.WorkSessionCreate, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):

    new_exercise = models.Exercise(**exercise.dict())

    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)

    return new_exercise