from datetime import datetime

from sqlalchemy import event
from sqlalchemy.orm import class_mapper

from app import db

class TimestampMixin(object):
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)

    @staticmethod
    def cm_time(mapper, connection, target):
        target.created = datetime.utcnow()
        target.modified = datetime.utcnow()

    @staticmethod
    def m_time(mapper, connection, target):
        target.modified = datetime.utcnow()

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, "before_insert", cls.cm_time)
        event.listen(cls, "before_update", cls.m_time)


class Duplicable(object):
    _columns_notduplicable = []

    @property
    def columns_as_dict(self):
        all_columns = class_mapper(self.__class__).mapped_table.c
        duplicable_columns = filter(
            lambda c: c.name not in self._columns_notduplicable, all_columns
        )
        return dict((col.name, getattr(self, col.name)) for col in duplicable_columns)


class BaseModelMixin(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )
    is_active = db.Column(db.Boolean, default=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            db.session.refresh(self)
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def add_flush(self):
        try:
            db.session.add(self)
            db.session.flush()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def __str__(self):
        return "%s object (%s)" % (self.__class__.__name__, self.id)
