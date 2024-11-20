# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 20, 2024 04:27:09
# Database: sqlite:////tmp/tmp.bN9yGUPh0G-01JD3X4RQMQXK92JAG84HZPKQX/WineDiaryApp/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Person(SAFRSBaseX, Base):
    """
    description: Stores information about people with whom wine was shared.
    """
    __tablename__ = 'people'
    _s_collection_name = 'Person'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    TastingSessionList : Mapped[List["TastingSession"]] = relationship(back_populates="person")



class Wine(SAFRSBaseX, Base):
    """
    description: Stores information about different wines tasted.
    """
    __tablename__ = 'wines'
    _s_collection_name = 'Wine'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    vintage = Column(Integer)
    grape_variety = Column(String)
    region = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    TastingSessionList : Mapped[List["TastingSession"]] = relationship(back_populates="wine")
    WineReviewList : Mapped[List["WineReview"]] = relationship(back_populates="wine")



class TastingSession(SAFRSBaseX, Base):
    """
    description: Tracks tasting sessions where wines are sampled with people.
    """
    __tablename__ = 'tasting_sessions'
    _s_collection_name = 'TastingSession'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    wine_id = Column(ForeignKey('wines.id'), nullable=False)
    person_id = Column(ForeignKey('people.id'), nullable=False)
    tasting_date = Column(Date, nullable=False)

    # parent relationships (access parent)
    person : Mapped["Person"] = relationship(back_populates=("TastingSessionList"))
    wine : Mapped["Wine"] = relationship(back_populates=("TastingSessionList"))

    # child relationships (access children)



class WineReview(SAFRSBaseX, Base):
    """
    description: Stores detailed reviews for wines, including ratings and tasting notes.
    """
    __tablename__ = 'wine_reviews'
    _s_collection_name = 'WineReview'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    wine_id = Column(ForeignKey('wines.id'), nullable=False)
    review_date = Column(Date, nullable=False)
    rating = Column(Integer)
    notes = Column(String)

    # parent relationships (access parent)
    wine : Mapped["Wine"] = relationship(back_populates=("WineReviewList"))

    # child relationships (access children)
