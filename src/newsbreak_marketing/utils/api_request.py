import httpx

from newsbreak_marketing.exceptions.api import APIRequestException, APIResponseException
from newsbreak_marketing.settings import ROOT_URL

async def request(method:str, url:str, headers:dict, json:dict|None = None, params:list|None = None, data:dict|None = None, files=None) -> dict:
    url = f'{ROOT_URL}/{url}'
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(method,url, headers=headers, json=json, params=params, data=data, files=files)            
    except httpx.RequestError as e:
        raise APIRequestException(str(e), -1)
    
    response = response.json()

    code = response.get('code')

    if code is None:
        raise APIRequestException(response.get('error'),response.get('status'))
    
    if code != 0:
        if response.get('errList'):
            raise APIResponseException(response.get('errList'), code)
        elif response.get('errMsg'):
            raise APIResponseException(response.get('errMsg'), code)
        else:
            raise APIResponseException(str(response), code)

    return response.get('data')