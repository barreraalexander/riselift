from fastapi import status, HTTPException, Response, Depends, APIRouter

from server import models, schemas, oauth2
from server.database import get_db
from sqlalchemy.orm import Session

from typing import List

router = APIRouter(
    prefix = "/worksessions",
    tags = ['Work Sessions']    
)

@router.get("/", response_model=List[schemas.WorkSession])
# def get_worksessions(db: Session = Depends(get_db)):
def get_worksessions(db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    worksessions = db.query(models.WorkSession).filter(models.WorkSession.owner_id==current_user.id).all()
    # worksessions = db.query(models.WorkSession).filter(models.WorkSession.owner_id==6).all()
    return worksessions

@router.get("/{id}", response_model=schemas.WorkSession)
def get_worksession(id: int, db: Session=Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):

    worksession = db.query(models.WorkSession).filter(models.WorkSession.id==id).first()

    if not worksession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Work Sesssion was not found')

    if worksession.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not authorized to perform requested action')

    return worksession



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.WorkSession)
# def create_worksession(workout: schemas.WorkSessionCreate, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
def create_worksession(workout: schemas.WorkSessionCreate, db: Session = Depends(get_db)):

    # new_worksession = models.WorkSession(owner_id=current_user.id, **workout.dict())
    new_worksession = models.WorkSession(owner_id=1, **workout.dict())

    db.add(new_worksession)
    db.commit()
    db.refresh(new_worksession)

    return new_worksession


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_worksession(id: int, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    
    worksession_query = db.query(models.WorkSession).filter(models.WorkSession.id == id)

    worksession = worksession_query.first()

    if worksession==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work Session was not found")

    if worksession.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    worksession_query.delete(synchronize_session=False)    
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}", response_model=schemas.WorkSession)
# def update_worksession(id: int, updated_worksession: schemas.WorkSessionCreate, db: Session = Depends(get_db)):
def update_worksession(id: int, updated_worksession: schemas.WorkSessionCreate, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):

    worksession_query = db.query(models.WorkSession).filter(models.WorkSession.id == id)

    worksession = worksession_query.first()

    if worksession==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work session was not found") 

    if worksession.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    worksession_query.update(updated_worksession.dict(), synchronize_session=False)

    db.commit()

    return worksession_query.first()