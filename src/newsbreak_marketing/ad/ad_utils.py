from typing import List

from newsbreak_marketing.core.base import APISession
from newsbreak_marketing.ad.schema import Creative, AdAuditStatus, CreativeType, AdAuditStatus
from newsbreak_marketing.core.schema import Status
from newsbreak_marketing.utils.api_request import request



class Ad(APISession):
    """
    This for creating Ad object

    ### Args:
        - `ad_set_id` (str): AdSet id
        - `ad_account_id` (str): Ad account id
        - `api_version` Optional(str): API version want to use or same as in `APISession`

    ### Attributes:
        - `id` (str|None): Ad id
        - `name` (str|None): Ad name
        - `ad_account_id` (str): Ad account id
        - `campaign_id` (str|None): Campaign id
        - `ad_set_id` (str): AdSet id
        - `click_tracking_url` (List[str]|None): Click tracking url
        - `impression_tracking_url` (List[str]|None): Impression tracking url
        - `status` (Status|None): Ad status
        - `audit_status` (AdAuditStatus|None): Ad audit status
        - `status_txt` (str|None): Ad status text
        - `creative` (Creative|None): Ad creative

    ### Functions:
        - `create`: For creating an ad
        - `update`: For updating an ad
        - `update_status`: For updating ad status
        - `delete`: For deleting an ad
        - `get`: For getting an ad
    """
    def __init__(self, ad_set_id:str, ad_account_id:str, api_version:str|None = None):
        if api_version:
            self.api_version = api_version
        self.id: str|None = None
        self.name : str|None = None
        self.ad_account_id: str = ad_account_id
        self.campaign_id: str|None = None
        self.ad_set_id: str = ad_set_id
        self.click_tracking_url: List[str]|None = None
        self.impression_tracking_url: List[str]|None = None
        self.status: Status|None = None
        self.audit_status: AdAuditStatus|None = None
        self.status_txt: str|None = None
        self.creative: Creative|None = None

        self.headers = {
            'Content-Type': 'application/json',
            'Access-Token': self.access_token
        }

    def _maker(self, data):
        self.id = data['id']
        self.name = data['name']
        self.campaign_id = data['campaignId']
        self.click_tracking_url = data.get('clickTrackingUrl')
        self.impression_tracking_url = data.get('impressionTrackingUrl')
        self.status = Status(data['status'])
        self.audit_status = AdAuditStatus(data['auditStatus'])
        self.status_txt = data.get('statusTxt')
        if data.get('creative'):
            self.creative = Creative(**data['creative'])
            self.type = CreativeType(data['creative']['type'])
        if data.get('type'):
            self.type = CreativeType(data['type'])

        return self
    
    async def create(
            self,
            name:str,
            type:CreativeType,
            headline:str,
            asset_url:str,
            description:str,
            call_to_action:str,
            brand_name:str,
            click_through_url:str,
            height:int|None = None,
            width:int|None = None,
            logo_url:str|None = None,
            cover_url:str|None = None,
            click_tracking_url:List[str]|None = None,
            impression_tracking_url:List[str]|None = None
            ):
        """
        For creating an ad

        ### Args:
            - `name` (str): Ad name
            - `type` (CreativeType): Ad creative type
            - `headline` (str): Ad creative headline
            - `asset_ulr` (str): Ad creative asset url
            - `description` (str): Ad creative description
            - `call_to_action` (str): Ad creative call to action
            - `brand_name` (str): Ad creative brand name
            - `click_through_url` (str): Ad creative click through url
            - `height` (int|None): Ad creative height, only when Ad type `CreativeType.VIDEO` 
            - `width` (int|None): Ad creative width, only when Ad type `CreativeType.VIDEO` 
            - `logo_url` Optional(str|None): Ad creative logo url
            - `cover_url` (str|None): Ad creative cover url, only when Ad type `CreativeType.VIDEO` 
            - `click_tracking_url` Optional(List[str]|None): Click tracking url
            - `impression_tracking_url` Optional(List[str]|None): Impression tracking url

        ### Returns:
            - `Ad`: Ad
        """
        
        if type == CreativeType.VIDEO:
            if height is None or width is None or cover_url is None:
                raise ValueError('height and width are required for video creative')

        url = f'{self.api_version}/ad/create'    

        payloads = {
            "name": name,
            "adSetId": self.ad_set_id,
            "creative": {
                "headline": headline,
                "assetUrl": asset_url,
                "description": description,
                "callToAction": call_to_action,
                "brandName": brand_name,
                "clickThroughUrl": click_through_url,
                "type": type.value
            }
        }

        if height:
            payloads['creative']['height'] = height
        if width:
            payloads['creative']['width'] = width
        if logo_url:
            payloads['creative']['logoUrl'] = logo_url
        if cover_url:
            payloads['creative']['coverUrl'] = cover_url
        if logo_url:
            payloads['creative']['logoUrl'] = logo_url
        if click_tracking_url:
            payloads['clickTrackingUrl'] = click_tracking_url
        if impression_tracking_url:
            payloads['impressionTrackingUrl'] = impression_tracking_url

        data = await request('POST', url, self.headers, json=payloads)

        return self._maker(data)
    
    async def delete(self,ad_id:str):
        """
        For deleting an ad

        ### Args:
            - `ad_id` (str): Ad id

        ### Returns:
            - `Ad`: A ad object
        """
        url = f'{self.api_version}/ad/delete/{ad_id}'

        data = await request('DELETE', url, self.headers)

        return self._maker(data)

    async def get(self, ad_id:str):
        """
        For getting an Ad

        ### Args:
            - `ad_id` (str): Ad id

        ### Returns:
            - `Ad`: A ad object
        """
        url = f'{self.api_version}/ad/getList'

        params = [
            ('adAccountId',self.ad_account_id),
            ('search',ad_id),
            ('pageNo',1),
            ('pageSize',1)
        ]
        
        data = await request('GET', url, self.headers, params=params)

        ad = data['rows'][0]

        return self._maker(ad)

    async def update_status(self,ad_id:str, status:Status):
        """
        For updating Ad status

        ### Args:
            - `ad_id` (str): Ad id
            - `status` (Status): Ad status

        ### Returns:
            - `Ad`: A ad object
        """
        url = f'{self.api_version}/ad/updateStatus/{ad_id}'

        payload = {
            "status": status.value
        }
        
        data = await request('PUT', url, self.headers, json=payload)

        return self._maker(data)
    
    async def update(
            self,
            ad_id:str,
            name:str,
            type:CreativeType,
            headline:str,
            asset_ulr:str,
            description:str,
            call_to_action:str,
            brand_name:str,
            click_through_url:str,
            height:int|None = None,
            width:int|None = None,
            cover_url:str|None = None,
            logo_url:str|None = None,
            click_tracking_url:List[str]|None = None,
            impression_tracking_url:List[str]|None = None,
            ):
        """
        For updating an Ad

        ### Args:
            - `ad_id` (str): Ad id
            - `name` (str): Ad name
            - `type` (CreativeType): Ad creative type
            - `headline` (str): Ad creative headline
            - `asset_ulr` (str): Ad creative asset url
            - `description` (str): Ad creative description
            - `call_to_action` (str): Ad creative call to action
            - `brand_name` (str): Ad creative brand name
            - `click_through_url` (str): Ad creative click through url
            - `height` (int|None): Ad creative height, only when Ad type `CreativeType.VIDEO` 
            - `width` (int|None): Ad creative width, only when Ad type `CreativeType.VIDEO` 
            - `cover_url` (str|None): Ad creative cover url, only when Ad type `CreativeType.VIDEO` 
            - `logo_url` Optional(str|None): Ad creative logo url
            - `click_tracking_url` Optional(List[str]|None): Ad creative click tracking url
            - `impression_tracking_url` Optional(List[str]|None): Ad creative impression tracking url

        ### Returns:
            - `Ad`: A ad object
        """
        
        if type == CreativeType.VIDEO:
            if height is None or width is None or cover_url is None:
                raise ValueError('height and width are required for video creative')
            
        url = f'{self.api_version}/ad/update/{ad_id}'

        payloads = {
            "name": name,
            "creative": {
                "headline": headline,
                "assetUrl": asset_ulr,
                "description": description,
                "callToAction": call_to_action,
                "brandName": brand_name,
                "clickThroughUrl": click_through_url,
                "type": type.value
            }
        }

        if height:
            payloads['creative']['height'] = height
        if width:
            payloads['creative']['width'] = width
        if cover_url:
            payloads['creative']['coverUrl'] = cover_url
        if logo_url:
            payloads['creative']['logoUrl'] = logo_url
        if click_tracking_url:
            payloads['clickTrackingUrl'] = click_tracking_url
        if impression_tracking_url:
            payloads['impressionTrackingUrl'] = impression_tracking_url

        data = await request('PUT', url, self.headers, json=payloads)

        return self._maker(data)