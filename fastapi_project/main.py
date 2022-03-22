from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas

from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/index')
async def index():
    return 'Welcome to StarCraft2 builds!'


@app.post('/builds', response_model=schemas.BuildForResponse)
def create_build(build: schemas.Build, db: Session = Depends(get_db)):
    return crud.create_build(db, build)


@app.get('/builds', response_model=list[schemas.BuildForResponse])
def get_builds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    builds = crud.get_builds(db, skip, limit)
    return builds


@app.get('/builds/{build_id}', response_model=schemas.BuildForResponse)
def get_build(build_id: int, db: Session = Depends(get_db)):
    build = crud.get_build(db, build_id)
    if not build:
        raise HTTPException(status_code=404, detail=f'Build {build_id} not found!')

    return build


@app.put('/builds', response_model=schemas.BuildForResponse)
def update_build(build: schemas.BuildToUpdate, db: Session = Depends(get_db)):
    updated = crud.update_build(db, build)
    if not updated:
        raise HTTPException(status_code=404, detail=f'Build {build.id} not found!')

    return updated


@app.delete('/builds/{build_id}')
def delete_build(build_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_build(db, build_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f'Build {build_id} not found!')

    return f'Build {build_id} deleted!'
