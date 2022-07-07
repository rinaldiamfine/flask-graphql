from app.graphql.object import (
    CampaignObject,
    CampaignNotificationObject,
    CampaignUserNotificationObject,
    CampaignNotificationSettingsObject,
    CampaignNotificationSettingUsersObject,
    CampaignNotificationFilesObject
)
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # # Allow only single column sorting
    # employees = SQLAlchemyConnectionField(
    #     Employee.connection, sort=Employee.sort_argument())
    # # Allows sorting over multiple columns, by default over the primary key
    # roles = SQLAlchemyConnectionField(Role.connection)
    # # Disable sorting over this field
    # campaigns = SQLAlchemyConnectionField(CampaignObject.connection, sort=None)
    campaignNotifications = SQLAlchemyConnectionField(CampaignNotificationObject.connection, sort=CampaignNotificationObject.sort_argument())
    campaignUserNotifications = SQLAlchemyConnectionField(CampaignUserNotificationObject.connection)

schema = graphene.Schema(query=Query)