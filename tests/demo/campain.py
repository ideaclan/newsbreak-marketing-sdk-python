import strawberry

@strawberry.type
class SMCampaign:

    @strawberry.field
    def createCampaign(self):
        