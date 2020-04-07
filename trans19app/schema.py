import graphene
from server.schema import Query as ApiQuery, Mutation as ApiMutation


class Query(graphene.ObjectType, ApiQuery):
    pass


class Mutation(graphene.ObjectType, ApiMutation):
    pass


graphql_schema = graphene.Schema(query=Query, mutation=Mutation)
