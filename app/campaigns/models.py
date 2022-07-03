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
    is_deleted = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return '<id : %s>' % (self.id)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def values(self):
        rv = dict()
        rv['id'] = self.id
        rv['uuid'] = self.uuid
        rv['slug'] = self.slug
        rv['is_deleted'] = self.is_deleted
        return rv