import os
import sys
from datetime import datetime, timedelta
from app import db
from app.mixins import TimestampMixin
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import ForeignKeyConstraint

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

class CampaignNotification(db.Model, TimestampMixin):
    __tablename__ = 'core_campaign_notifications'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))

    notification_sent_unique_users = db.Column(db.Integer)
    notification_sent_count = db.Column(db.Integer)
    notification_click_unique_users = db.Column(db.Integer)
    notification_click_count = db.Column(db.Integer)

    is_deleted = db.Column(db.Boolean(), default=False)
    deleted = db.Column(db.DateTime())

    # user_notification_ids = relationship('CampaignUserNotification')
    # notif = db.Column(db.Integer, primary_key=True)
    # __table_args__ = (
    #     ForeignKeyConstraint(
    #         ["id"],
    #         ["core_campaign_user_notifications.id"]
    #     ),
    # )

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

class CampaignNotificationSettings(db.Model, TimestampMixin):
    __tablename__ = 'core_campaign_notification_settings'

    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer)
    from_random_number = db.Column(db.Integer)
    to_random_number = db.Column(db.Integer)
    user_type = db.Column(db.String(255))
    user_preference = db.Column(db.String(255))
    use_segmentation = db.Column(db.Boolean(), default=True)
    current_file_id = db.Column(db.Integer(), db.ForeignKey('core_campaign_notification_settings.id'))

    is_deleted = db.Column(db.Boolean(), default=False)
    deleted = db.Column(db.DateTime())

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
        result_value["batch"] = self.batch
        result_value["from_random_number"] = self.from_random_number
        result_value["to_random_number"] = self.to_random_number
        result_value["user_type"] = self.user_type
        result_value["user_preference"] = self.user_preference
        result_value["use_segmentation"] = self.use_segmentation
        result_value["current_file_id"] = self.current_file_id
        # result_value["created"] = self.created
        # result_value["modified"] = self.modified
        return result_value

class CampaignNotificationSettingUsers(db.Model, TimestampMixin):
    __tablename__ = 'core_campaign_notification_setting_users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    file_id = db.Column(db.Integer(), db.ForeignKey('core_campaign_notification_settings.id'))
    setting_id = db.Column(db.Integer(), db.ForeignKey('core_campaign_notification_settings.id'))

    is_deleted = db.Column(db.Boolean(), default=False)
    deleted = db.Column(db.DateTime())

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
        result_value["file_id"] = self.file_id
        result_value["setting_id"] = self.setting_id
        # result_value["created"] = self.created
        # result_value["modified"] = self.modified
        return result_value

class CampaignNotificationFiles(db.Model, TimestampMixin):
    __tablename__ = 'core_campaign_notification_files'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(500))
    file_name_akdoc = db.Column(db.String(500))
    batch = db.Column(db.Integer)

    is_deleted = db.Column(db.Boolean(), default=False)
    deleted = db.Column(db.DateTime())

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
        result_value["file_name"] = self.file_name
        result_value["file_name_akdoc"] = self.file_name_akdoc
        result_value["batch"] = self.batch
        # result_value["created"] = self.created
        # result_value["modified"] = self.modified
        return result_value