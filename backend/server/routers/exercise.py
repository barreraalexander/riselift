from fastapi import status, HTTPException, Response, Depends, APIRouter

from server import models, schemas, oauth2
from server.database import get_db
from sqlalchemy.orm import Session

from typing import List

router = APIRouter(
    prefix="/exercises",
    tags = ['Work Sessions']
)

@router.get("/", response_model=List[schemas.ExerciseOut])
# def get_exercises(db: Session = Depends(get_db)):
def get_exercises(db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    # if  not current_user:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    # exercises = db.query(models.Exercise).filter(models.Exercise.worksession_id==current_user.id).all()
    
    exercises = db.query(models.Exercise).filter(models.WorkSession.owner_id==current_user.id).all()


    # exercises = db.query(models.Exercise).all()
    return exercises

@router.get("/{id}", response_model=schemas.ExerciseOut)
def get_exercise(id: int, db: Session=Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    exercise = db.query(models.Exercise).filter(models.Exercise.id==id).first()
    


    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Exercise not Found')

    # if exercise.worksession.owner.id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not authorized to perform requested action')

    return exercise

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Exercise)
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
# def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):

    # new_exercise = models.Exercise(owner_id=1, **exercise.dict())
    new_exercise = models.Exercise(owner_id=current_user.id, **exercise.dict())
    
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)

    return new_exercise