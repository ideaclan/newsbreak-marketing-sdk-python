from newsbreak_marketing.core.base import APISession
from newsbreak_marketing.utils.api_request import request
from newsbreak_marketing.core.schema import Status
from newsbreak_marketing.ad_set.schema import AdSetBudgetType, AdSetBidType, AdSetDeliveryRate, Targeting, AdSetOnlineStatus

class AdSet(APISession):
    """
    This is child class `APISession` used to create a adSet object. A campaign is need for creating an adSet

    ### Args:
        - `ad_account_id` (int|str): Ad account id given by Newsbreak
        - `campaign_id` (int|str): Campaign id
        - `api_version` Optional(str): API version want to use or same as in `APISession`

    ### Attributes:
        - `id` (str|None): AdSet id
        - `org_id` (str|None): Organization id
        - `name` (str|None): AdSet name
        - `tracking_id` (str|None): AdSet tracking id
        - `budget` (int|None): AdSet budget
        - `status` (Status|None): AdSet status
        - `budget_type` (AdSetBudgetType|None): AdSet budget type
        - `start_time` (int|None): AdSet start time
        - `end_time` (int|None): AdSet end time
        - `schedule` (dict|None): AdSet schedule
        - `bid_type` (AdSetBidType|None): AdSet bid type
        - `bid_rate` (int|None): AdSet bid rate
        - `delivery_rate` (AdSetDeliveryRate|None): AdSet delivery rate
        - `optimization` (bool|None): AdSet optimization
        - `targeting` (Targeting|None): AdSet targeting

    ### Functions:
        - `create`: For creating a adSet
        - `delete`: For deleting a adSet
        - `update`: For updating a adSet
        - `update_status`: For updating adSet status
        - `get`: For getting a adSet details
    """
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
        """
        For creating a adSet

        ### Args:
            - `name` (str): AdSet name
            - `budget_type` (AdSetBudgetType): AdSet budget type
            - `budget` (int): AdSet budget
            - `start_time` (int): AdSet start time
            - `end_time` (int): AdSet end time
            - `bid_type` (AdSetBidType): AdSet bid type
            - `bit_rate` (int): AdSet bid rate
            - `delivery_rate` (AdSetDeliveryRate): AdSet delivery rate
            - `targeting` (Targeting): AdSet targeting
            - `tracking_id` (str): AdSet tracking id
            - `optimization` Optional(bool): AdSet optimization

        ### Returns:
            - `AdSet`: A adSet object
        """
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
            "targeting": targeting.model_dump(exclude_none=True, by_alias=True),
            "trackingId": tracking_id
        }

        data = await request('POST', url, self.headers, json=payload)

        return self._maker(data)
    
    async def delete(self, ad_set_id:str):
        """
        For deleting a adSet

        ### Args:
            - `ad_set_id` (str): AdSet id

        ### Returns:
            - `AdSet`: A adSet object
        """
        url = f'{self.api_version}/ad-set/delete/{ad_set_id}'

        data = await request('DELETE', url, self.headers)

        return self._maker(data)
    
    async def get(self,ad_set_id:str):
        """
        For getting adSet details

        ### Args:
            -`ad_set_id` (str): AdSet id
        ### Returns:
            -`AdSet`: A adSet object
         
        """
        url = f'{self.api_version}/ad-set/getList'

        params = [
            ('adAccountId',self.ad_account_id),
            ('search',ad_set_id),
            ('pageNo',1),
            ('pageSize',1)
        ]
        
        data = await request('GET', url, self.headers, params=params)

        ad_set = data['list'][0]

        return self._maker(ad_set)
    
    async def update_status(self,ad_set_id:str, status:Status):
        """
        For updating adSet status

        ### Args:
            - `ad_set_id` (str): AdSet id
            - `status` (Status): AdSet status

        ### Returns:
            - `AdSet`: A adSet object
        """
        self.id = ad_set_id

        url = f'{self.api_version}/ad-set/updateStatus/{self.id}'

        payload = {
            "status": status.value
        }
        
        data = await request('PUT', url, self.headers, json=payload)

        return self._maker(data)
    
    async def update(self,
                     ad_set_id:str,
                     name:str,
                     budget_type:AdSetBudgetType,
                     budget:int,
                     start_time:int,
                     end_time:int,
                     bid_type:AdSetBidType,
                     bit_rate:int,
                     delivery_rate:AdSetDeliveryRate,
                     tracking_id:str,
                     targeting:Targeting,
                     optimization:bool = True
                     ):
        """
        For updating a adSet
        
        ### Args:
            - `ad_set_id` (str): AdSet id
            - `name` (str): AdSet name
            - `budget_type` (AdSetBudgetType): AdSet budget type
            - `budget` (int): AdSet budget
            - `start_time` (int): AdSet start time
            - `end_time` (int): AdSet end time
            - `bid_type` (AdSetBidType): AdSet bid type
            - `bit_rate` (int): AdSet bid rate
            - `delivery_rate` (AdSetDeliveryRate): AdSet delivery rate
            - `tracking_id` (str): AdSet tracking id
            - `targeting` (Targeting): AdSet targeting
            - `optimization` Optional(bool): AdSet optimization

        ### Returns:
            - `AdSet`: A adSet object
        """
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
            "targeting": targeting.model_dump(exclude_none=True, by_alias=True)
        }
        print(f"Payload for update: {payload}")
        if tracking_id:
            payload['trackingId'] = tracking_id

        data = await request('PUT', url, self.headers, json=payload)

        return self._maker(data)
    