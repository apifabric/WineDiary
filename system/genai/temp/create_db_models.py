# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Wine(Base):
    """description: Stores information about different wines tasted."""
    __tablename__ = 'wines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    vintage = Column(Integer)
    grape_variety = Column(String)
    region = Column(String)

    def __repr__(self):
        return f"<Wine(name='{self.name}', vintage='{self.vintage}')>"


class Person(Base):
    """description: Stores information about people with whom wine was shared."""
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)

    def __repr__(self):
        return f"<Person(name='{self.name}', email='{self.email}')>"


class WineReview(Base):
    """description: Stores detailed reviews for wines, including ratings and tasting notes."""
    __tablename__ = 'wine_reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    wine_id = Column(Integer, ForeignKey('wines.id'), nullable=False)
    review_date = Column(Date, nullable=False)
    rating = Column(Integer)
    notes = Column(String)

    def __repr__(self):
        return f"<WineReview(wine_id='{self.wine_id}', rating='{self.rating}')>"


class TastingSession(Base):
    """description: Tracks tasting sessions where wines are sampled with people."""
    __tablename__ = 'tasting_sessions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    wine_id = Column(Integer, ForeignKey('wines.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    tasting_date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<TastingSession(wine_id='{self.wine_id}', person_id='{self.person_id}')>"


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

# Test data for Wine
wine1 = Wine(name="Cabernet Sauvignon", vintage=2015, grape_variety="Cabernet Sauvignon", region="Napa Valley")
wine2 = Wine(name="Merlot", vintage=2017, grape_variety="Merlot", region="Bordeaux")
wine3 = Wine(name="Pinot Noir", vintage=2018, grape_variety="Pinot Noir", region="Oregon")
wine4 = Wine(name="Chardonnay", vintage=2016, grape_variety="Chardonnay", region="Sonoma")

# Test data for Person
person1 = Person(name="John Doe", email="john.doe@example.com")
person2 = Person(name="Jane Smith", email="jane.smith@example.com")
person3 = Person(name="Emily Clark", email="emily.clark@example.com")
person4 = Person(name="Michael Brown", email="michael.brown@example.com")

# Test data for WineReview
review1 = WineReview(wine_id=1, review_date=date(2023, 1, 15), rating=8, notes="Fruity with oakiness")
review2 = WineReview(wine_id=2, review_date=date(2023, 2, 25), rating=7, notes="Smooth and rich")
review3 = WineReview(wine_id=3, review_date=date(2023, 3, 10), rating=9, notes="Light and floral")
review4 = WineReview(wine_id=4, review_date=date(2023, 4, 20), rating=6, notes="Crisp and dry")

# Test data for TastingSession
tasting1 = TastingSession(wine_id=1, person_id=1, tasting_date=date(2023, 5, 10))
tasting2 = TastingSession(wine_id=2, person_id=2, tasting_date=date(2023, 5, 15))
tasting3 = TastingSession(wine_id=3, person_id=3, tasting_date=date(2023, 5, 20))
tasting4 = TastingSession(wine_id=4, person_id=4, tasting_date=date(2023, 5, 25))



session.add_all([wine1, wine2, wine3, wine4, person1, person2, person3, person4, review1, review2, review3, review4])
session.commit()
