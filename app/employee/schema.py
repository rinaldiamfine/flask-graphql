from app.employee.models import Department as DepartmentModel
from app.employee.models import Employee as EmployeeModel
from app.employee.models import Role as RoleModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )

class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    employees = SQLAlchemyConnectionField(
        Employee.connection, sort=Employee.sort_argument())
    # Allows sorting over multiple columns, by default over the primary key
    roles = SQLAlchemyConnectionField(Role.connection)
    # Disable sorting over this field
    departments = SQLAlchemyConnectionField(Department.connection, sort=None)


schema = graphene.Schema(query=Query)