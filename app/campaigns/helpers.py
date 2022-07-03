from .models import Campaign
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

class CampaignList:
    def __init__(self, api=None, method=None, limit=None, offset=None):
        self.api = api
        self.method = method
        self.limit = limit
        self.offset = offset

    def get_list(self):
        campaigns_query = Campaign.query.filter_by(is_deleted=False).limit(self.limit).offset(self.offset)
        total = campaigns_query.count()
        campaigns = campaigns_query.all()
        campaignlist = list()
        for campaign in campaigns:
            rv = campaign.values()
            campaignlist.append(rv)
        resp = dict()
        resp['data'] = campaignlist
        resp['total'] = total
        return True, resp
