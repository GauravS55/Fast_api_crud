from pydantic import BaseModel, HttpUrl
from typing import Optional
from fastapi import Form

class CropSchema(BaseModel):
    crop_name: Optional[str] = None
    stages: Optional[str] = None
    days: Optional[int] = None
    image: Optional[HttpUrl] = None
    title: Optional[str] = None
    task_to_perform: Optional[str] = None

    @classmethod
    def as_form(cls, 
        crop_name: Optional[str] = Form(None),
        stages: Optional[str] = Form(None),
        days: Optional[int] = Form(None),
        image: Optional[HttpUrl] = Form(None),
        title: Optional[str] = Form(None),
        task_to_perform:Optional[str] = Form(None), 
 
        ):
        return cls(
            crop_name=crop_name, 
            stages=stages, 
            days=days,
            image=image,
            title=title,
            task_to_perform=task_to_perform,
        )

class CropPutSchema(BaseModel):
    crop_name: str 
    stages: str 
    days: int 
    image: HttpUrl
    title: str 
    task_to_perform: str 

    @classmethod
    def as_form(cls, 
        crop_name: str = Form(...),
        stages: str = Form(...),
        days: int = Form(...),
        image: HttpUrl = Form(...),
        title: str = Form(...),
        task_to_perform:str = Form(...), 
 
        ):
        return cls(
            crop_name=crop_name, 
            stages=stages, 
            days=days,
            image=image,
            title=title,
            task_to_perform=task_to_perform,
        )

    