from pydantic import BaseModel

class StudentBase(BaseModel):
    sname: str | None = None
    saddr:  str

class StudentCreate(StudentBase):
    sclass: str

class Student(StudentBase):
    sno: str

    class Config:
        orm_mode = True