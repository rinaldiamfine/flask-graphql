from flask import Blueprint
from flask_restful import Api
from .api import (
    CampaignApi,
)
# from app.campaigns.schema import schema as CampaignSchema
# from flask_graphql import GraphQLView
# from app import app

campaigns_blueprint = Blueprint(
    "campaigns", __name__, url_prefix="/api/v1/campaigns"
)
campaigns_api = Api(campaigns_blueprint)
campaigns_api.add_resource(CampaignApi, "")
# campaigns_api.add_resource(CampaignGraphApi, "/graphql")
# app.add_url_rule(
#     "/graphql", view_func=GraphQLView.as_view("graphql", schema=CampaignSchema, graphiql=True)
# )