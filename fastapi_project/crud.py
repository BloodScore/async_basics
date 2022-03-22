from sqlalchemy import update
from sqlalchemy.orm import Session

import models
import schemas


def get_build(db: Session, build_id: int):
    return db.query(models.Build).filter(models.Build.id == build_id).first()


def get_builds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Build).offset(skip).limit(limit).all()


def create_build(db: Session, build: schemas.Build):
    opponents = ''
    for o in build.opponents:
        opponents += o.value + ' '

    new_build = models.Build(
        name=build.name,
        description=build.description,
        race=build.race.value,
        type=build.type.value,
        opponents=opponents
    )

    db.add(new_build)
    db.commit()
    db.refresh(new_build)

    return new_build


def update_build(db: Session, build: schemas.BuildToUpdate):
    build_to_update = db.query(models.Build).filter(models.Build.id == build.id).first()

    if not build_to_update:
        return False

    opponents = ''
    for o in build.opponents:
        opponents += o.value + ' '

    update_statement = update(models.Build).where(models.Build.id == build.id)\
        .values(
            name=build.name,
            description=build.description,
            race=build.race.value,
            type=build.type.value,
            opponents=opponents
        ).execution_options(synchronize_session="fetch")

    db.execute(update_statement)
    db.commit()
    db.refresh(build_to_update)

    return build_to_update


def delete_build(db: Session, build_id: int):
    build_to_delete = db.query(models.Build).filter(models.Build.id == build_id).first()
    if build_to_delete:
        db.delete(build_to_delete)
        db.commit()
        return True
    else:
        return False
