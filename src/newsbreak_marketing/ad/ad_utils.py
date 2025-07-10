from typing import List

from newsbreak_marketing.core.base import APISession
from newsbreak_marketing.ad.schema import Creative, AdAuditStatus, CreativeType, AdAuditStatus
from newsbreak_marketing.core.schema import Status
from newsbreak_marketing.utils.api_request import request



class Ad(APISession):
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
        if data.get('type'):
            self.type = CreativeType(data['type'])

        return self
    
    async def create(
            self,
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
            logo_url:str|None = None,
            cover_url:str|None = None,
            click_tracking_url:List[str]|None = None,
            impression_tracking_url:List[str]|None = None
            ):
        
        if type == CreativeType.VIDEO:
            if height is None or width is None or cover_url is None:
                raise ValueError('height and width are required for video creative')

        url = f'{self.api_version}/ad/create'    

        payloads = {
            "name": name,
            "adSetId": self.ad_set_id,
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
    
    async def delete(self,id:str):
        url = f'{self.api_version}/ad/delete/{id}'

        data = await request('DELETE', url, self.headers)

        return self._maker(data)

    async def get(self, id:str):
        url = f'{self.api_version}/ad/getList'

        params = [
            ('adAccountId',self.ad_account_id),
            ('search',id),
            ('pageNo',1),
            ('pageSize',1)
        ]
        
        data = await request('GET', url, self.headers, params=params)

        ad = data['rows'][0]

        return self._maker(ad)

    async def update_status(self,id:str, status:Status):
        url = f'{self.api_version}/ad/updateStatus/{id}'

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