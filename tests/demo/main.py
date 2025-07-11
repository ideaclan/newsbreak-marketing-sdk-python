from newsbreak_marketing import APISession
import strawberry
from strawberry.asgi import GraphQL

from .campaign import SMCampaign, SQCampaign

session = APISession(access_token='3d8a7a49-bb3e-4201-b03b-29d0a1f3b348')

@strawberry.type
class Mutation(SMCampaign):
    ...

@strawberry.type
class Query(SQCampaign):
    ...

schema = strawberry.federation.Schema( query=Query, mutation=Mutation)

app = GraphQL(schema)


