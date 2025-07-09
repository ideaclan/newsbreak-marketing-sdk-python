import httpx

from newsbreak_marketing.exceptions.api import APIRequestException, APIResponseException
from newsbreak_marketing.settings import ROOT_URL

async def request(method:str, url:str, headers:dict, json:dict|None = None, params:list|None = None, data:dict|None = None, files=None) -> dict:
    url = f'{ROOT_URL}/{url}'
    
    async with httpx.AsyncClient() as client:
        response = await client.request(method,url, headers=headers, json=json, params=params, data=data, files=files)            
    
    
    response = response.json()

    code = response.get('code')

    if code is None:
        raise APIRequestException(response.get('error'),response.get('status'))
    
    if code != 0:
        raise APIResponseException(response.get('errList'), code)

    return response.get('data')