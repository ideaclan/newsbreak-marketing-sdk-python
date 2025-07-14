from newsbreak_marketing import APISession
import strawberry
from strawberry.asgi import GraphQL
import uvicorn

from campaign import SMCampaign, SQCampaign
from ad_set import SMAdSet, SQAdSet
from ad import SMAd, SQAd

session = APISession(access_token='3d8a7a49-bb3e-4201-b03b-29d0a1f3b348')

@strawberry.type
class Mutation(SMCampaign, SMAdSet, SMAd):
    ...

@strawberry.type
class Query(SQCampaign, SQAdSet, SQAd):
    ...

schema = strawberry.federation.Schema( query=Query, mutation=Mutation)

from strawberry.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.applications import Starlette

import strawberry


graphql_app = GraphQL(schema)

# Wrap in a Starlette app with middleware
app = Starlette(
    routes=[],
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Or restrict as needed
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
)

# Mount the GraphQL app
app.mount("/", graphql_app)

# print(schema.as_str())

# Run with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
