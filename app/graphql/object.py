from app.campaigns.models import Campaign
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

class CampaignObject(SQLAlchemyObjectType):
    class Meta:
        model = Campaign
        interfaces = (relay.Node, )