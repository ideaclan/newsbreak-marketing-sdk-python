import httpx

from newsbreak_marketing.exceptions.api import APIRequestException, APIResponseException
from newsbreak_marketing.settings import ROOT_URL

async def request(method:str, url:str, headers:dict, json:dict|None = None, params:list|None = None, data:dict|None = None) -> dict:
    url = f'{ROOT_URL}/{url}'
    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(method,url, headers=headers, json=json, params=params, data=data)            
    except httpx.HTTPStatusError as e:
        raise APIRequestException(e.response.text, e.response.status_code)
    
    response = response.json()

    code = response.get('code')
    if code != 0:
        raise APIResponseException(response.get('errMsg'), code)

    return response.get('data')