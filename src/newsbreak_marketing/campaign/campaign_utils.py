import httpx
from typing import List, Tuple

from newsbreak_marketing.core.base import APISession
from newsbreak_marketing.campaign.schema import CampaignObjective, CampaignOnlineStatus
from newsbreak_marketing.utils.api_request import request
from newsbreak_marketing.core.schema import Status

class Campaign(APISession):
    async def __init__(self, ad_account_id:int|str):
        super().__init__()
        self.ad_account_id: str = str(ad_account_id)
        self.id: str|None = None
        self.org_id: str|None = None
        self.name: str|None = None
        self.objective: CampaignObjective|None = None
        self.status: Status|None = None
        self.budget = ...

        self.headers = {
            'Content-Type': 'application/json',
            'Access-Token': self.access_token
        }

    async def get(self, campaign_id:int|str) -> "Campaign":
        url = f'{self.api_version}/campaign/getList'

        params = [
            ('adAccountId',self.ad_account_id),
            ('search',campaign_id),
            ('onlineStatus',CampaignOnlineStatus.ACTIVE.value),
            ('onlineStatus',CampaignOnlineStatus.INACTIVE.value),
            ('onlineStatus',CampaignOnlineStatus.DELETE.value),
            ('onlineStatus',CampaignOnlineStatus.WARNING.value),
            ('pageNo',1),
            ('pageSize',1)
        ]

        data = await request('GET', url, self.headers, params=params)

        camp = data['rows'][0]

        self.org_id = camp['orgId']
        self.name = camp['name']
        self.create_time = camp['createTime']
        self.update_time = camp['updateTime']
        self.objective = CampaignObjective(camp['objective'])
        self.budget = camp['budget']
        self.status = Status(camp['status'])

        return self
        
        

    async def create(self,name:str, ad_account_id:int|str, objective:CampaignObjective) -> "Campaign":
        url = f'{self.api_version}campaign/create'

        payloads = {
            "name": name,
            "adAccountId": int(ad_account_id),
            "objective": objective.value
        }

        data = await request('POST', url, self.headers, json=payloads)

        self.id = data['id']
        self.org_id = data['orgId']
        self.name = data['name']
        self.objective = CampaignObjective(data['objective'])
        self.budget = data['budget']
        self.online_status = CampaignOnlineStatus(data['onlineStatus'])
        self.status = Status(data['status'])


        return self
    
    
    async def delete(self, campaign_id:int|str) -> "Campaign":
        url = f'{self.api_version}/campaign/delete/{campaign_id}'

        data = await request('DELETE', url, self.headers)

        self.id = data['id']
        self.org_id = data['orgId']
        self.name = data['name']
        self.objective = CampaignObjective(data['objective'])
        self.budget = data['budget']
        self.online_status = CampaignOnlineStatus(data['onlineStatus'])
        self.status = Status(data['status'])

        return self

    async def get_list(self, campaign_id:int|str,online_statues:List[CampaignOnlineStatus],page_no:int,page_size:int) -> Tuple[List["Campaign"],int,bool]:
        url = f'{self.api_version}/campaign/getList'

        params = [
            ('adAccountId',self.ad_account_id),
            ('search',campaign_id),
            ('pageNo',page_no),
            ('pageSize',page_size)
        ] + [('onlineStatus',status.value) for status in online_statues]

        data = await request('GET', url, self.headers, params=params)

        rows = data['rows']

        campaigns = []

        for camp in rows:
            c = Campaign(self.ad_account_id)

            c.id = camp['id']
            self.org_id = camp['orgId']
            self.name = camp['name']
            self.create_time = camp['createTime']
            self.update_time = camp['updateTime']
            self.objective = CampaignObjective(camp['objective'])
            self.budget = camp['budget']
            self.status = Status(camp['status'])

            campaigns.append(c)

        return campaigns, data['total'], data['hasNext']