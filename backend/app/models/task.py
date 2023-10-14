from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value, values):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid objectid")
        return str(value)


class Task(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        populate_by_name = True
        from_attributes = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "id": "605af4637762914091f1dabc",  # Ejemplo de ObjectId
                "title": "Ejemplo de tarea",
                "description": "Descripción de la tarea",
                "completed": True
            }
        }


class UpdateTask(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = False

    class Config:
        populate_by_name = True
        from_attributes = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "id": "605af4637762914091f1dabc",  # Ejemplo de ObjectId
                "title": "Ejemplo de tarea",
                "description": "Descripción de la tarea",
                "completed": True
            }
        }
