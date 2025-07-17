from enum import Enum
import strawberry
from newsbreak_marketing import Status
from newsbreak_marketing.campaign import CampaignObjective, CampaignOnlineStatus
from newsbreak_marketing.ad_set import Targeting, AdSetBudgetType, AdSetBudgetType, AdSetDeliveryRate, AdSetBidType
from newsbreak_marketing.ad import AdAuditStatus, Creative, CreativeType
from typing import Optional, List
from example.demo.utils import model_to_dataclass, model_to_dataclass_st_type



@strawberry.type
class STCampaign:
    id: strawberry.ID
    org_id: strawberry.ID
    name: str
    objective: strawberry.enum(CampaignObjective) # type: ignore
    online_status: strawberry.enum(CampaignOnlineStatus) # type: ignore
    status: strawberry.enum(Status) # type: ignore

# BudgetType = strawberry.enum(AdSetBudgetType)
# BidType = strawberry.enum(AdSetBidType)
# DeliveryRate = strawberry.enum(AdSetDeliveryRate)
# Status = strawberry.enum(Status)


@strawberry.type
class STAdSet:
    id: strawberry.ID
    name: str
    org_id: strawberry.ID
    ad_account_id: strawberry.ID
    campaign_id: strawberry.ID
    tracking_id: strawberry.ID
    budget: int
    budget_type: strawberry.enum(AdSetBudgetType) # type: ignore
    start_time: int
    end_time: int
    bid_type: strawberry.enum(AdSetBidType) # type: ignore
    bid_rate: int
    delivery_rate: strawberry.enum(AdSetDeliveryRate) # type: ignore
    optimization: bool
    status: strawberry.enum(Status) # type: ignore
    # targeting: strawberry.enum(Targeting) # type: ignore


@strawberry.type
class STAd:
    id: strawberry.ID
    name: str
    campaign_id: strawberry.ID
    click_tracking_url: Optional[List[str]] = None
    impression_tracking_url: Optional[List[str]] = None
    status: strawberry.enum(Status) # type: ignore
    audit_status: strawberry.enum(AdAuditStatus) # type: ignore
    status_txt: Optional[str] = None
    creative: Optional[model_to_dataclass_st_type(Creative)] = None # type: ignore
    type: Optional[strawberry.enum(CreativeType)] = None # type: ignore