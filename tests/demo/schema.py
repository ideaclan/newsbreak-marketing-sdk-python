from enum import Enum
import strawberry
from newsbreak_marketing import Status
from newsbreak_marketing.campaign import CampaignObjective, CampaignOnlineStatus



@strawberry.type
class STCampaign:
    id: strawberry.ID
    org_id: strawberry.ID
    name: str
    objective: strawberry.enum(CampaignObjective) # type: ignore
    online_status: strawberry.enum(CampaignOnlineStatus) # type: ignore
    status: strawberry.enum(Status) # type: ignore