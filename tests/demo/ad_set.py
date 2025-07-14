import strawberry
from newsbreak_marketing.ad_set import AdSet, AdSetBudgetType, AdSetBidType, AdSetDeliveryRate, Targeting
from newsbreak_marketing import Status
from util2 import model_to_dataclass, print_dataclass_fields_info
from typing import Optional
from dataclasses import asdict

from schema import STAdSet


@strawberry.type
class SMAdSet:
    tar = model_to_dataclass(Targeting)

    BudgetType = strawberry.enum(AdSetBudgetType)
    BidType = strawberry.enum(AdSetBidType)
    DeliveryRate = strawberry.enum(AdSetDeliveryRate)

    @strawberry.mutation
    async def create_ad_set(
        self,
        campaign_id: str,
        ad_account_id: str,
        name: str,
        budget_type: BudgetType, # type: ignore
        budget: int,
        start_time: int,
        end_time: int,
        bid_type: BidType, # type: ignore
        bit_rate: int,
        delivery_rate: DeliveryRate, # type: ignore
        tracking_id: str,
        targeting: Optional[tar]= None, # type: ignore
        optimization: bool = True,
    ) -> STAdSet:
        if targeting is None:
            targeting = SMAdSet.tar()
        ad_set = AdSet(campaign_id=campaign_id, ad_account_id=ad_account_id)

        tara = Targeting(**asdict(targeting))

        ad_set = await ad_set.create(
            name=name,
            budget_type=AdSetBudgetType(budget_type.value), # type: ignore
            budget=budget,
            start_time=start_time,
            end_time=end_time,
            bid_type=AdSetBidType(bid_type.value), # type: ignore
            bit_rate=bit_rate,
            delivery_rate=AdSetDeliveryRate(delivery_rate.value), # type: ignore
            tracking_id=tracking_id,
            optimization=optimization,
            targeting=tara
        )

        return STAdSet(
            id=ad_set.id,
            name=ad_set.name,
            org_id=ad_set.org_id,
            ad_account_id=ad_set.ad_account_id,
            campaign_id=ad_set.campaign_id,
            tracking_id=ad_set.tracking_id,
            budget=ad_set.budget,
            budget_type=ad_set.budget_type,
            start_time=ad_set.start_time,
            end_time=ad_set.end_time,
            bid_type=ad_set.bid_type,
            bid_rate=ad_set.bid_rate,
            delivery_rate=ad_set.delivery_rate,
            optimization=ad_set.optimization,
            status=ad_set.status
        )
    
    @strawberry.mutation
    async def update_ad_set(
        self,
        campaign_id: str,
        ad_account_id: str,
        ad_set_id: str,
        name: str,
        budget_type: BudgetType, # type: ignore
        budget: int,
        start_time: int,
        end_time: int,
        bid_type: BidType, # type: ignore
        bit_rate: int,
        delivery_rate: DeliveryRate, # type: ignore
        tracking_id: str,
        targeting: Optional[tar] = None, # type: ignore
        optimization: bool = True
    ) -> STAdSet:
        if targeting is None:
            targeting = SMAdSet.tar()
        
        tara = Targeting(**asdict(targeting))

        ad_set = AdSet(ad_account_id=ad_account_id, campaign_id=campaign_id)

        ad_set = await ad_set.update(
            ad_set_id=ad_set_id,
            name=name,
            budget_type=AdSetBudgetType(budget_type.value), # type: ignore
            budget=budget,
            start_time=start_time,
            end_time=end_time,
            bid_type=AdSetBidType(bid_type.value), # type: ignore
            bit_rate=bit_rate,
            delivery_rate=AdSetDeliveryRate(delivery_rate.value), # type: ignore
            tracking_id=tracking_id,
            targeting=tara,
            optimization=optimization
        )

        return STAdSet(
            id=ad_set.id,
            name=ad_set.name,
            org_id=ad_set.org_id,
            ad_account_id=ad_set.ad_account_id,
            campaign_id=ad_set.campaign_id,
            tracking_id=ad_set.tracking_id,
            budget=ad_set.budget,
            budget_type=ad_set.budget_type,
            start_time=ad_set.start_time,
            end_time=ad_set.end_time,
            bid_type=ad_set.bid_type,
            bid_rate=ad_set.bid_rate,
            delivery_rate=ad_set.delivery_rate,
            optimization=ad_set.optimization,
            status=ad_set.status
        )
    
    @strawberry.mutation
    async def update_ad_set_status(
        self,
        ad_set_id: str,
        ad_account_id: str,
        campaign_id: str,
        status: strawberry.enum(Status) # type: ignore
    ) -> STAdSet:
        ad_set = AdSet(ad_account_id=ad_account_id, campaign_id=campaign_id)

        ad_set = await ad_set.update_status(
            ad_set_id=ad_set_id,
            status=Status(status.value) # type: ignore
        )

        return STAdSet(
            id=ad_set.id,
            name=ad_set.name,
            org_id=ad_set.org_id,
            ad_account_id=ad_set.ad_account_id,
            campaign_id=ad_set.campaign_id,
            tracking_id=ad_set.tracking_id,
            budget=ad_set.budget,
            budget_type=ad_set.budget_type,
            start_time=ad_set.start_time,
            end_time=ad_set.end_time,
            bid_type=ad_set.bid_type,
            bid_rate=ad_set.bid_rate,
            delivery_rate=ad_set.delivery_rate,
            optimization=ad_set.optimization,
            status=ad_set.status
        )


@strawberry.type
class SQAdSet:
    @strawberry.field
    async def get_ad_set(
        self,
        ad_set_id: str,
        ad_account_id: str,
        campaign_id: str
        ) -> STAdSet:

        ad_set = AdSet(ad_account_id=ad_account_id, campaign_id=campaign_id)

        ad_set = await ad_set.get(ad_set_id=ad_set_id)

        return STAdSet(
            id=ad_set.id,
            name=ad_set.name,
            org_id=ad_set.org_id,
            ad_account_id=ad_set.ad_account_id,
            campaign_id=ad_set.campaign_id,
            tracking_id=ad_set.tracking_id,
            budget=ad_set.budget,
            budget_type=ad_set.budget_type,
            start_time=ad_set.start_time,
            end_time=ad_set.end_time,
            bid_type=ad_set.bid_type,
            bid_rate=ad_set.bid_rate,
            delivery_rate=ad_set.delivery_rate,
            optimization=ad_set.optimization,
            status=ad_set.status
        )