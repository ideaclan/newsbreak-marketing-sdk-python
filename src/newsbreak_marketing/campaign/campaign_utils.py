from newsbreak_marketing.core.base import APISession
from newsbreak_marketing.campaign.schema import CampaignObjective, CampaignOnlineStatus
from newsbreak_marketing.utils.api_request import request
from newsbreak_marketing.core.schema import Status

class Campaign(APISession):
    """This is child class `APISession` used to create a campaign object

    ### Args:
        - `ad_account_id` (int|str): Ad account id given by Newsbreak
        - `api_version` Optional(str): API version want to use or same as in `APISession`

    ### Attributes:
        - `id` (str|None): Campaign id
        - `org_id` (str|None): Organization id
        - `name` (str|None): Campaign name
        - `objective` (CampaignObjective|None): Campaign objective
        - `budget` (int|None): Campaign budget
        - `online_status` (CampaignOnlineStatus|None): Campaign online status
        - `status` (Status|None): Campaign status

    ### Functions:
        - `create`: For creating a campaign
        - `delete`: For deleting a campaign
        - `update`: For updating a campaign
        - `update_status`: For updating campaign status
        - `get`: For getting a campaign details
    """
    def __init__(self, ad_account_id:str,api_version:str|None = None):
        self.ad_account_id: str = ad_account_id
        if api_version:
            self.api_version=api_version
        self.id: str|None = None
        self.org_id: str|None = None
        self.name: str|None = None
        self.objective: CampaignObjective|None = None
        self.status: Status|None = None
        self.budget: int|None = None
        self.online_status: CampaignOnlineStatus|None = None
        self.status: Status|None = None

        self.headers = {
            'Content-Type': 'application/json',
            'Access-Token': self.access_token
        }

    def _maker(self,data):
        self.id = data['id']
        self.org_id = data['orgId']
        self.name = data['name']
        self.objective = CampaignObjective(data['objective'])
        self.budget = data.get('budget')
        self.online_status = CampaignOnlineStatus(data['onlineStatus'])
        self.status = Status(data['status'])

        return self

    async def get(self, campaign_id:int|str) -> "Campaign":
        """For getting campaign details

        ### Args:
            - `campaign_id` (int|str): Campaign id

        ### Returns:
            - `Campaign`: A campaign object

        """
        url = f'{self.api_version}/campaign/getList'

        params = [
            ('adAccountId',self.ad_account_id),
            ('search',campaign_id),
            ('pageNo',1),
            ('pageSize',1)
        ]

        data = await request('GET', url, self.headers, params=params)

        camp = data['list'][0]

        return self._maker(camp)
        
        

    async def create(self,name:str, objective:CampaignObjective) -> "Campaign":
        """For creating a campaign

        ### Args:
            - `name` (str): Campaign name
            - `objective` (CampaignObjective): Campaign objective

        ### Returns:
            - `Campaign`: A campaign object
        """
        url = f'{self.api_version}/campaign/create'

        payloads = {
            "name": name,
            "adAccountId": self.ad_account_id,
            "objective": objective.value
        }

        data = await request('POST', url, self.headers, json=payloads)

        return self._maker(data)
    
    
    async def delete(self, campaign_id:int|str) -> "Campaign":
        """For deleting a campaign

        ### Args:
            - `campaign_id` (int|str): Campaign id

        ### Returns:
            - `Campaign`: A campaign object
        """
        url = f'{self.api_version}/campaign/delete/{campaign_id}'

        data = await request('DELETE', url, self.headers)

        return self._maker(data)

    
    async def update(self, campaign_id:int|str, name:str) -> "Campaign":
        """For Updating a campaign

        ### Args:
            - `campaign_id` (int|str): Campaign id
            - `name` (str): Campaign name

        ### Returns:
            - `Campaign`: A campaign object
        """
        url = f'{self.api_version}/campaign/update/{campaign_id}'

        payload = {
            "name": name
        }

        data = await request('PUT', url, self.headers, json=payload)

        return self._maker(data)
    
    async def update_status(self, campaign_id:int|str,status:Status) -> "Campaign":
        """
        For updating campaign status

        ### Args:
            - `campaign_id` (int|str): Campaign id
            - `status` (Status): Campaign status

        ### Returns:
            - `Campaign`: A campaign object
        """
        url = f'{self.api_version}/campaign/updateStatus/{campaign_id}'

        payload = {
            "status": status.value
        }

        data = await request('PUT', url, self.headers, json=payload)

        return self._maker(data)