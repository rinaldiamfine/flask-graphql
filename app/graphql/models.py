import os
import sys
from datetime import datetime, timedelta
from app import db
from app.mixins import TimestampMixin
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, func
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

class CampaignNotification(Base):
    __tablename__ = 'core_campaign_notifications'

    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True)
    name = Column(String)

    notification_sent_unique_users = Column(Integer)
    notification_sent_count = Column(Integer)
    notification_click_unique_users = Column(Integer)
    notification_click_count = Column(Integer)

    is_deleted = Column(Boolean(), default=False)
    deleted = Column(DateTime())

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

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def values(self):
        result_value = dict()
        result_value["id"] = self.id
        result_value["uuid"] = self.uuid
        # result_value["name"] = self.name
        result_value["notification_sent_unique_users"] = self.notification_sent_unique_users
        result_value["notification_sent_count"] = self.notification_sent_count
        result_value["notification_click_unique_users"] = self.notification_click_unique_users
        result_value["notification_click_count"] = self.notification_click_count
        # result_value["created"] = self.created
        # result_value["modified"] = self.modified
        return result_value

class CampaignUserNotification(db.Model, TimestampMixin):
    __tablename__ = 'core_campaign_user_notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    user_email = db.Column(db.String(255))
    campaign_notification_id = db.Column(db.Integer(), db.ForeignKey('core_campaign_notifications.id'))
    content_email = db.Column(db.Text())
    random_group_number = db.Column(db.Integer())

    sent_action = db.Column(db.Boolean(), default=False)
    click_action = db.Column(db.Boolean(), default=False)
    is_deleted = db.Column(db.Boolean(), default=False)
    deleted = db.Column(db.DateTime())

    campaign_notification = relationship(
        CampaignNotification,
        backref=backref('core_campaign_notifications',
                        uselist=True,
                        cascade='delete,all'))

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

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def values(self):
        result_value = dict()
        result_value["id"] = self.id
        result_value["user_id"] = self.user_id
        result_value["user_email"] = self.user_email
        result_value["campaign_notification_id"] = self.campaign_notification_id
        result_value["content_email"] = self.content_email
        result_value["random_group_number"] = self.random_group_number
        result_value["sent_action"] = self.sent_action
        result_value["click_action"] = self.click_action
        # result_value["created"] = self.created
        # result_value["modified"] = self.modified
        return result_value