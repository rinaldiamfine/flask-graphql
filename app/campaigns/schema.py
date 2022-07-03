# from app.campaigns.models import Campaign as CampaignModel

# import graphene
# from graphene import relay
# from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

# class Campaigns(SQLAlchemyObjectType):
#     class Meta:
#         model = CampaignModel
#         interfaces = (relay.Node, )


# class Query(graphene.ObjectType):
#     node = relay.Node.Field()
#     # # Allow only single column sorting
#     # employees = SQLAlchemyConnectionField(
#     #     Employee.connection, sort=Employee.sort_argument())
#     # # Allows sorting over multiple columns, by default over the primary key
#     # roles = SQLAlchemyConnectionField(Role.connection)
#     # # Disable sorting over this field
#     campaigns = SQLAlchemyConnectionField(Campaigns.connection, sort=None)


# schema = graphene.Schema(query=Query)