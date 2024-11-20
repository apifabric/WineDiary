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
    """description: Table for storing details about various wines."""
    __tablename__ = 'wine'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    vintage = Column(Integer, nullable=True)
    winery = Column(String, nullable=True)
    varietal = Column(String, nullable=True)
    country = Column(String, nullable=True)


class Review(Base):
    """description: Table for storing details about wine reviews."""
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    wine_id = Column(Integer, ForeignKey('wine.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    review_date = Column(DateTime, nullable=False)
    notes = Column(String, nullable=True)


class Person(Base):
    """description: Table for storing details about people participating in wine tasting."""
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)


class Event(Base):
    """description: Table for storing wine tasting events."""
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_date = Column(Date, nullable=False)
    location = Column(String, nullable=True)
    description = Column(String, nullable=True)


class WineTasting(Base):
    """description: Intermediary table linking wine tastings to specific wines."""
    __tablename__ = 'wine_tasting'

    id = Column(Integer, primary_key=True, autoincrement=True)
    wine_id = Column(Integer, ForeignKey('wine.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    wine_notes = Column(String, nullable=True)


class Participant(Base):
    """description: Intermediary table linking people to wine tasting events."""
    __tablename__ = 'participant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date, datetime

# Test data for Wine table
wine1 = Wine(name="Chardonnay", vintage=2018, winery="ABC Winery", varietal="Chardonnay", country="USA")
wine2 = Wine(name="Merlot", vintage=2016, winery="XYZ Vineyards", varietal="Merlot", country="France")
wine3 = Wine(name="Cabernet Sauvignon", vintage=2017, winery="South Villa", varietal="Cabernet Sauvignon", country="Australia")
wine4 = Wine(name="Pinot Noir", vintage=2019, winery="RedHill", varietal="Pinot Noir", country="New Zealand")

# Test data for Review table
review1 = Review(wine_id=1, rating=92, review_date=datetime(2023, 10, 20), notes="Well-balanced with oak notes.")
review2 = Review(wine_id=2, rating=87, review_date=datetime(2023, 10, 15), notes="Fruity with a hint of spice.")
review3 = Review(wine_id=3, rating=90, review_date=datetime(2023, 09, 12), notes="Full-bodied and rich.")
review4 = Review(wine_id=4, rating=85, review_date=datetime(2023, 08, 30), notes="Light with cherry aromas.")

# Test data for Person table
person1 = Person(name="Alice Smith", email="alice@example.com", phone="123-456-7890")
person2 = Person(name="Bob Johnson", email="bob@example.com", phone="098-765-4321")
person3 = Person(name="Charlie Brown", email="charlie@example.com", phone="456-789-0123")
person4 = Person(name="Diana Prince", email="diana@example.com", phone="321-654-0987")

# Test data for Event table
event1 = Event(event_date=date(2023, 10, 22), location="Rioja Room", description="Fall wine tasting event.")
event2 = Event(event_date=date(2023, 09, 14), location="Napa Hall", description="Annual wine gala.")
event3 = Event(event_date=date(2023, 08, 25), location="Bordeaux Base", description="Vintage wine night.")
event4 = Event(event_date=date(2023, 07, 16), location="Mosel Lounge", description="Summer wine showcase.")

# Test data for WineTasting table
wine_tasting1 = WineTasting(wine_id=1, event_id=1, wine_notes="Perfectly chilled.")
wine_tasting2 = WineTasting(wine_id=2, event_id=2, wine_notes="Paired well with cheese.")
wine_tasting3 = WineTasting(wine_id=3, event_id=3, wine_notes="Aged beautifully.")
wine_tasting4 = WineTasting(wine_id=4, event_id=4, wine_notes="Smooth finish.")

# Test data for Participant table
participant1 = Participant(person_id=1, event_id=1)
participant2 = Participant(person_id=2, event_id=2)
participant3 = Participant(person_id=3, event_id=3)
participant4 = Participant(person_id=4, event_id=4)


session.add_all([wine1, wine2, wine3, wine4, review1, review2, review3, review4, person1, person2, person3, person4, event1, event2, event3, event4, wine_tasting1, wine_tasting2, wine_tasting3, wine_tasting4, participant1, participant2, participant3, participant4])
session.commit()
