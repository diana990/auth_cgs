from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    username: str = Field(...)
    full_name: str = Field(...)
    password: str = Field(...)

    class Config:
         schema_extra = {
            "example": {
                "full_name": "Diana",
                "username": "diana",
                "password": "admin"
            }
    }
         
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
         schema_extra = {
            "example": {
                "email": "diana@gmail.com",
                "password": "admin"
            }
    }
         
class PostSchema(BaseModel):
     title: str = Field(...)
     description: str = Field(...)
     author: str = Field(...)

     class Config:
          schema_extra = {
               "example": {
                    "title": "Cats",
                    "description": "All about cats",
                    "author": "Rimma"
               }
          }