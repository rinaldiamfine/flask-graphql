import os
import sys
from datetime import datetime, timedelta
from app import db
from app.mixins import TimestampMixin

class Campaign(db.Model, TimestampMixin):
    __tablename__ = 'core_campaigns'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255), unique=True)
    slug = db.Column(db.String(500))