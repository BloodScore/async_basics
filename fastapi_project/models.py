from sqlalchemy import Column, Integer, String, Text

from database import Base


class Build(Base):
    __tablename__ = 'builds'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    description = Column(Text)
    race = Column(String(255))
    type = Column(String(255))
    opponents = Column(String(255))
