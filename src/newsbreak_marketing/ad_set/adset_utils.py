from newsbreak_marketing.core.base import APISession
from newsbreak_marketing.utils.api_request import request
from newsbreak_marketing.core.schema import Status
from newsbreak_marketing.ad_set.schema import AdSetBudgetType, AdSetBidType, AdSetDeliveryRate, Targeting, AdSetOnlineStatus

class AdSet(APISession):
    def __init__(self, campaign_id:int|str , ad_account_id:str, api_version:str|None = None):
        self.campaign_id: str = str(campaign_id)
        if api_version:
            self.api_version=api_version
        self.id: str|None = None
        self.org_id: str|None = None
        self.ad_account_id: str|None = ad_account_id
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
        self.targeting: Targeting|None = None

        self.headers = {
            'Content-Type': 'application/json',
            'Access-Token': self.access_token
        }
        

    def _maker(self, data):

        self.id = data['id']
        self.name = data['name']
        self.org_id = data['orgId']
        self.ad_account_id = data['adAccountId']
        self.campaign_id = data['campaignId']
        self.tracking_id = data['trackingId']
        self.budget = data['budget']
        self.budget_type = AdSetBudgetType(data['budgetType'])
        self.status = Status(data['status'])
        self.start_time = data['startTime']
        self.end_time = data['endTime']
        self.bid_type = AdSetBidType(data['bidType'])
        self.bid_rate = data['bidRate']
        self.delivery_rate = AdSetDeliveryRate(data['deliveryRate'])
        self.optimization = data['optimization']
        self.targeting = Targeting(**data['targeting'])

        return self


    async def create(
            self,
            name:str,
            budget_type:AdSetBudgetType,
            budget:int,
            start_time:int,
            end_time:int,
            bid_type:AdSetBidType,
            bit_rate:int,
            delivery_rate:AdSetDeliveryRate,
            targeting:Targeting,
            tracking_id:str,
            optimization:bool = True,
            ):
        url = f'{self.api_version}/ad-set/create'

        payload = {
            "campaignId": self.campaign_id,
            "name": name,
            "budgetType": budget_type.value,
            "budget": budget,
            "startTime": start_time,
            "endTime": end_time,
            "bidType": bid_type.value,
            "bidRate": bit_rate,
            "deliveryRate": delivery_rate.value,
            "optimization": optimization,
            "targeting": targeting.model_dump(exclude_none=True),
            "trackingId": tracking_id
        }

        data = await request('POST', url, self.headers, json=payload)

        return self._maker(data)
    
    async def delete(self, id:str):
        url = f'{self.api_version}/ad-set/delete/{id}'

        data = await request('DELETE', url, self.headers)

        return self._maker(data)
    
    async def get(self,ad_set_id:str):
        url = f'{self.api_version}/ad-set/getList'

        params = [
            ('adAccountId',self.ad_account_id),
            ('search',ad_set_id),
            ('pageNo',1),
            ('pageSize',1)
        ]
        
        data = await request('GET', url, self.headers, params=params)

        ad_set = data['rows'][0]

        return self._maker(ad_set)
    
    async def update_status(self, status:Status):
        url = f'{self.api_version}/ad-set/updateStatus/{self.id}'

        payload = {
            "status": status.value
        }
        
        data = await request('PUT', url, self.headers, json=payload)

        return self._maker(data)
    
    async def update(self, ad_set_id:str, name:str, budget_type:AdSetBudgetType, budget:int, start_time:int, end_time:int, bid_type:AdSetBidType, bit_rate:int, delivery_rate:AdSetDeliveryRate, targeting:Targeting,optimization:bool = True, tracking_id:str|None = None):
        url = f'{self.api_version}/ad-set/update/{ad_set_id}'

        payload = {
            "campaignId": self.campaign_id,
            "name": name,
            "budgetType": budget_type.value,
            "budget": budget,
            "startTime": start_time,
            "endTime": end_time,
            "bidType": bid_type.value,
            "bidRate": bit_rate,
            "deliveryRate": delivery_rate.value,
            "optimization": optimization,
            "targeting": targeting.model_dump(exclude_none=True)
        }

        if tracking_id:
            payload['trackingId'] = tracking_id

        data = await request('PUT', url, self.headers, json=payload)

        return self._maker(data)
    