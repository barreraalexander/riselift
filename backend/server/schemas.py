from pydantic import BaseModel, EmailStr

from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    id: int
    email: EmailStr
    upldate: datetime

    class Config:
        orm_mode = True


class WorkSessionBase(BaseModel):
    name: str
    owner: UserOut

class WorkSessionCreate(WorkSessionBase):
    pass

class WorkSession(WorkSessionBase):
    id: int
    upldate: datetime
    owner_id: int
    # owner: UserOut
    exercises: str = None

    class Config:
        orm_mode = True




class UserCreate(BaseModel):
    email: EmailStr
    password: str
    

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]


class WorkSessionOut(BaseModel):
    id: int
    name: str
    session_begin: datetime
    session_end: datetime
    exercises: str = None
    owner: UserOut
    # WorkSession: WorkSession

    class Config:
        orm_mode = True



class ExerciseBase(BaseModel):
    name: str
    list_index: int
    rep_count: int
    weight: float
    weight_type: str
    worksession_id: int


class ExerciseCreate(ExerciseBase):
    pass

class Exercise(ExerciseBase):
    id: int
    # worksession_id: int
    worksession: WorkSessionOut

    # owner_id: int
    # owner: UserOut


    class Config:
        orm_mode = True


class ExerciseOut(BaseModel):
    Exercise: Exercise

    class Config:
        orm_mode = True

