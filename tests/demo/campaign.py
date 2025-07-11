import strawberry
from newsbreak_marketing.campaign import Campaign, CampaignObjective
from newsbreak_marketing import Status
from .schema import STCampaign

@strawberry.type
class SMCampaign:

    @strawberry.mutation
    async def create_Campaign(
        self,
        name:str,
        ad_account_id:str,
        objective:strawberry.enum(CampaignObjective) # type: ignore
    )-> STCampaign:
        camp = Campaign(ad_account_id=ad_account_id)

        camp = await camp.create(
            name=name,
            objective=objective
        )

        return STCampaign(
            id=camp.id, # type: ignore
            org_id=camp.org_id, # type: ignore
            name=camp.name, # type: ignore
            objective=camp.objective,
            online_status=camp.online_status,
            status=camp.status
        )
    
    @strawberry.mutation
    async def update_campaign(
        self,
        account_id:str,
        campaign_id:str,
        name:str
    )-> STCampaign:
        camp = Campaign(ad_account_id=account_id)

        camp = await camp.update(
            campaign_id=campaign_id,
            name=name
        )

        return STCampaign(
            id=camp.id, # type: ignore
            org_id=camp.org_id, # type: ignore
            name=camp.name, # type: ignore
            objective=camp.objective,
            online_status=camp.online_status,
            status=camp.status
        )

    @strawberry.mutation
    async def update_campaign_status(
        self,
        account_id:str,
        campaign_id:str,
        status:strawberry.enum(Status) # type: ignore
    )-> STCampaign:
        camp = Campaign(ad_account_id=account_id)

        camp = await camp.update_status(
            campaign_id=campaign_id,
            status=status
        )

        return STCampaign(
            id=camp.id, # type: ignore
            org_id=camp.org_id, # type: ignore
            name=camp.name, # type: ignore
            objective=camp.objective,
            online_status=camp.online_status,
            status=camp.status
        )
    

@strawberry.type
class SQCampaign:
    @strawberry.field
    async def get_campaign(
        self,
        ad_account_id:str,
        campaign_id:str
    )-> STCampaign:
        camp = Campaign(ad_account_id)

        camp = await camp.get(campaign_id=campaign_id)

        return STCampaign(
            id=camp.id, # type: ignore
            org_id=camp.org_id, # type: ignore
            name=camp.name, # type: ignore
            objective=camp.objective,
            online_status=camp.online_status,
            status=camp.status
        )