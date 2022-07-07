from app.campaigns.models import (
    Campaign,
    CampaignNotification,
    CampaignUserNotification,
    CampaignNotificationSettings,
    CampaignNotificationSettingUsers,
    CampaignNotificationFiles
)
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

class CampaignObject(SQLAlchemyObjectType):
    class Meta:
        model = Campaign
        interfaces = (relay.Node, )

class CampaignNotificationObject(SQLAlchemyObjectType):
    class Meta:
        model = CampaignNotification
        interfaces = (relay.Node, )

class CampaignUserNotificationObject(SQLAlchemyObjectType):
    class Meta:
        model = CampaignUserNotification
        interfaces = (relay.Node, )

class CampaignNotificationSettingsObject(SQLAlchemyObjectType):
    class Meta:
        model = CampaignNotificationSettings
        interfaces = (relay.Node, )

class CampaignNotificationSettingUsersObject(SQLAlchemyObjectType):
    class Meta:
        model = CampaignNotificationSettingUsers
        interfaces = (relay.Node, )

class CampaignNotificationFilesObject(SQLAlchemyObjectType):
    class Meta:
        model = CampaignNotificationFiles
        interfaces = (relay.Node, )
