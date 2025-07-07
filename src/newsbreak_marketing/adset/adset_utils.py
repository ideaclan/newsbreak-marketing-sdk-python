from newsbreak_marketing.core.base import APISession
from newsbreak_marketing.utils.api_request import request
from newsbreak_marketing.core.schema import Status
from newsbreak_marketing.adset.schema import AdSetBudgetType, AdSetBidType, AdSetDeliveryRate

class AdSet(APISession):
    def __init__(self, campaign_id:int|str ,api_version:str|None = None):
        self.campaign_id: str = str(campaign_id)
        if api_version:
            self.api_version=api_version
        self.id: str|None = None
        self.org_id: str|None = None
        self.ad_account_id: str|None = None
        self.name: str|None = None
        self.tracking_id: str|None = None
        self.budget: int|None = None
        self.status: Status|None = None
        self.budget_type: AdSetBudgetType|None = None
        self.start_time: int|None = None
        self.end_time: int|None = None
        self.schedule: dict|None = None
        self.bid_type: AdSetBidType|None = None
        self.bid_rate: int|None = None
        self.delivery_rate: AdSetDeliveryRate|None = None
        self.optimization: bool|None = None
        