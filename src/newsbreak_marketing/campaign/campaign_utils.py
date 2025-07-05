import httpx
from typing import Optional

from newsbreak_marketing.session.create import Session
from newsbreak_marketing.campaign.schema import CampaignObjective
from newsbreak_marketing.settings import ROOT_URL
from newsbreak_marketing.exceptions.general import APIRequestException, APIResponseException

class Campaign:
    def __init__(self, session:Session, api_version:Optional[str] = None):
        if not isinstance(session, Session):
            raise TypeError("session must be of type Session")
        self.session = session
        self.api_version = api_version or session.api_version

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.session.access_token
        }

    async def create(self,name:str, ad_account_id:int|str, objective:CampaignObjective) -> dict:
        url = f'{ROOT_URL}/{self.api_version}/campaign/create'

        payloads = {
            "name": name,
            "adAccountId": int(ad_account_id),
            "objective": objective.value
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, headers=self.headers, json=payloads)            
        except httpx.HTTPStatusError as e:
            raise APIRequestException(e.response.text, e.response.status_code)
        
        response = response.json()

        code = response.get('code')
        if code != 0:
            raise APIResponseException(response.get('errMsg'), code)

        return response.get('data')
    
    async def get(self, ad_account_id:int|str, page_no:int, page_size:int) -> dict:
        url = f'{ROOT_URL}/{self.api_version}/campaign/getList'

        params = {
            "adAccountId": int(ad_account_id),
            "pageNo": page_no,
            "pageSize": page_size
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=self.headers, params=params)            
        except httpx.HTTPStatusError as e:
            raise APIRequestException(e.response.text, e.response.status_code)
        
        response = response.json()

        code = response.get('code')
        if code != 0:
            raise APIResponseException(response.get('errMsg'), code)

        return response.get('data')
    
    async def delete(self, campaign_id:int|str) -> dict:
        url = f'{ROOT_URL}/{self.api_version}/campaign/delete/{campaign_id}'

        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(url, headers=self.headers)            
        except httpx.HTTPStatusError as e:
            raise APIRequestException(e.response.text, e.response.status_code)
        
        response = response.json()

        code = response.get('code')
        if code != 0:
            raise APIResponseException(response.get('errMsg'), code)

        return response.get('data')

