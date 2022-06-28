from app.employee.schema import schema
from flask_graphql import GraphQLView
from app import app

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)