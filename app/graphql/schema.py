from app.graphql.object import CampaignObject
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
    campaigns = SQLAlchemyConnectionField(CampaignObject.connection, sort=None)

schema = graphene.Schema(query=Query)