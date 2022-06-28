import imp
from database import db_session, init_db
from flask import Flask
from flask_graphql import GraphQLView
from app import models
# from app.employee import api

app = Flask(__name__)
app.debug = True

from app.employee.schema import schema
from flask_graphql import GraphQLView

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)