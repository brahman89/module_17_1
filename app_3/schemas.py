from pydantic import BaseModel


class CreateUser(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int


class CreateTask(BaseModel):
    id: int
    title: str
    content: str
    priority: str


class UpdateTask(BaseModel):
    id: int
    title: str
    content: str
    priority: str
