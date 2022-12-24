from pydantic import BaseModel, EmailStr

from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    upldate: datetime

    class Config:
        orm_mode = True


class WorkSessionBase(BaseModel):
    name: str
    # owner: UserOut

class WorkSessionCreate(WorkSessionBase):
    pass

class WorkSession(WorkSessionBase):
    id: int
    upldate: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True





class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    

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


class ExerciseCreate(ExerciseBase):
    worksession_id: int

class Exercise(ExerciseBase):
    id: int
    worksession_id: int
    # owner_id: int

    class Config:
        orm_mode = True


class ExerciseOut(Exercise):
    # id: int
    # name: str
    # list_index: int
    
    # worksession_id: int
    pass

    class Config:
        orm_mode = True

