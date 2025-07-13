import strawberry
from newsbreak_marketing.ad_set import AdSet, AdSetBudgetType, AdSetBidType, AdSetDeliveryRate, Targeting
from dataclasses import fields, is_dataclass
from util2 import model_to_dataclass, print_dataclass_fields_info
from typing import Optional


@strawberry.type
class SMAdSet:
    tar = model_to_dataclass(Targeting)

    @strawberry.mutation
    def create_ad_set(
        self,
        campaign_id: str,
        ad_account_id: str,
        name: str,
        budget_type: strawberry.enum(AdSetBudgetType), # type: ignore
        budget: int,
        start_time: int,
        end_time: int,
        bid_type: strawberry.enum(AdSetBidType), # type: ignore
        bit_rate: int,
        delivery_rate: strawberry.enum(AdSetDeliveryRate), # type: ignore
        tracking_id: str,
        targeting: Optional[tar]= None, # type: ignore
        optimization: bool = True,
    ) -> str:
        if targeting is None:
            targeting = SMAdSet.tar()
        ad_set = AdSet(campaign_id=campaign_id, ad_account_id=ad_account_id)
        print_dataclass_fields_info(targeting)

        return 'hello'