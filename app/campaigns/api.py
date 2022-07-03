import http.client
import json
import resource

import requests
import werkzeug
from flask import Response, request, redirect, render_template
from flask_restful import Api, Resource, reqparse
from marshmallow import ValidationError
from app import app
from .helpers import CampaignList
api = Api(app)

# class CampaignGraphApi(Resource):
#     def __init__(self):
#         self.reqparser = reqparse.RequestParser()
#         super(CampaignGraphApi, self).__init__()

#     def post(self):
#         print("POST")
    
#     def get(self):
#         print("GET")


class CampaignApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        super(CampaignApi, self).__init__()

    def get(self):
        try:
            param = dict()
            param['api'] = '/api/v1/campaigns'
            param['method'] = 'GET'
            param['limit'] = 10
            param['offset'] = 0
            status, result = CampaignList(**param).get_list()
            if not status:
                return Response(
                    json.dumps(result),
                    status=http.client.BAD_REQUEST,
                    mimetype='application/json'
                )

            return Response(
                json.dumps(result),
                status=http.client.OK,
                mimetype='application/json'
            )
        except Exception as e:
            return Response(
                json.dumps(str(e)),
                status=http.client.INTERNAL_SERVER_ERROR,
                mimetype='application/json'
            )