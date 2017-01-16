"""Crumby data models."""

from . import db

class ModelMixin(object):
   def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Calendar(db.Model, ModelMixin):
    """Date record."""
    __tablename__ = 'calendar'
    datetime = db.Column(db.DateTime, primary_key=True)

class Visit(db.Model, ModelMixin):
    """Page visit record."""
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(39))
    cid = db.Column(db.String(10))
    datetime = db.Column(db.DateTime)
    doc_title = db.Column(db.Text)
    doc_uri = db.Column(db.Text)
    doc_enc = db.Column(db.String(25))
    referrer = db.Column(db.Text)
    _referrer = db.Column(db.Text)
    platform = db.Column(db.String(25))
    browser = db.Column(db.String(25))
    version = db.Column(db.String(25))
    screen_res = db.Column(db.String(25))
    screen_depth = db.Column(db.String(10))
    continent = db.Column(db.String(3))
    country = db.Column(db.String(3))
    subdivision_1 = db.Column(db.String(75))
    subdivision_2 = db.Column(db.String(75))
    city = db.Column(db.String(75))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    accuracy_radius = db.Column(db.Integer)
    time_zone = db.Column(db.String(50))
    lang = db.Column(db.String(10))
    _lang = db.Column(db.String(10))

class Event(db.Model, ModelMixin):
    """Interaction event record."""
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(39))
    cid = db.Column(db.String(10))
    datetime = db.Column(db.DateTime)
    doc_title = db.Column(db.Text)
    doc_uri = db.Column(db.Text)
    name = db.Column(db.Text)
    value = db.Column(db.Text)
