import graphene
from server.schema import Query as ApiQuery


class Query(ApiQuery, graphene.ObjectType):
    pass


graphql_schema = graphene.Schema(query=Query)
