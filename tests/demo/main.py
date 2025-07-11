from newsbreak_marketing import APISession
import strawberry
from strawberry.asgi import GraphQL

from .campaign import SMCampaign

session = APISession(access_token='3d8a7a49-bb3e-4201-b03b-29d0a1f3b348')

@strawberry.type
class Mutation(SMCampaign):
    ...

schema = strawberry.federation.Schema(mutation=Mutation)

app = GraphQL(schema)


