from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy import create_engine
from database import Base, engine
from sqlalchemy.orm import Session
from models import Crop
from schemas import CropSchema, CropPutSchema


Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/get/")
def get_all():
    session = Session(bind=engine, expire_on_commit=False)

    crop_list = session.query(Crop).all()

    session.close()

    return crop_list

@app.post("/post/", status_code=status.HTTP_201_CREATED)
def create(crop: CropSchema = Depends(CropSchema.as_form)):
    session = Session(bind=engine, expire_on_commit=False)

    cropdb = Crop(crop_name = crop.crop_name, stages=crop.stages, days=crop.days, image=crop.image, title=crop.title, task_to_perform=crop.task_to_perform)

    session.add(cropdb)
    session.commit()

    id = cropdb.id

    session.close()

    return f"created todo item with id {id}"

@app.get("/get/{id}")
def read(id: int):
    session = Session(bind=engine, expire_on_commit=False)

    crop = session.query(Crop).get(id)

    session.close()

    if not crop:
        raise HTTPException(status_code=404, detail=f"crop item with id {id} not found")

    return crop

@app.put("/put/{id}")
def update(id: int, crop: CropPutSchema =  Depends(CropPutSchema.as_form)):
    session = Session(bind=engine, expire_on_commit=False)

    get_crop = session.query(Crop).get(id)

    if crop:
        get_crop.crop_name = crop.crop_name
        get_crop.stages=crop.stages
        get_crop.days=crop.days 
        get_crop.image=crop.image
        get_crop.title=crop.title 
        get_crop.task_to_perform=crop.task_to_perform
        session.commit()

    session.close()

    if not crop:
        raise HTTPException(status_code=404, detail=f"crop item with id {id} not found")

    return crop

@app.patch("/patch/{id}")
def update(id: int, crop: CropSchema =  Depends(CropSchema.as_form)):
    session = Session(bind=engine, expire_on_commit=False)

    get_crop = session.query(Crop).get(id)

    if crop:
        data = crop.dict(exclude_none=True)
        for key, value in data.items():
            setattr(get_crop, key, value)
        session.add(get_crop)
        session.commit()
        session.refresh(get_crop)
        return get_crop

    session.close()

@app.delete("/delete/{id}")
def delete(id: int):
    session = Session(bind=engine, expire_on_commit=False)

    get_crop = session.query(Crop).get(id)

    if get_crop:
        session.delete(get_crop)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"get_crop item with id {id} not found")

    return f"{id} Crop deleted"