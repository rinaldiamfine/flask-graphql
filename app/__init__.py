from flask_marshmallow import Marshmallow
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .BlueprintLoader import BlueprintLoader
# from app.middleware import ReverseProxied
# from app.BlueprintLoader import BlueprintLoader

app = Flask(__name__)
# app.wsgi_app = ReverseProxied(app.wsgi_app)
app.config.from_object("config")
db = SQLAlchemy(app)
app.debug = True

failed_imports = []
successful_imports = []
loader = BlueprintLoader().discover_blueprints_by_pattern()
for blueprint in loader:
    try:
        app.register_blueprint(blueprint)
        successful_imports.append(blueprint)
    except Exception as e:
        failed_imports.append(blueprint)

from app import models

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()


# from app.employee.schema import schema
# from flask_graphql import GraphQLView

# app.add_url_rule(
#     "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
# )