from newsbreak_marketing.utils.api_request import request
async def upload(session, ad_account_id:int|str, media, api_version:str|None = None):
    api_version = api_version or session.api_version
    url = f'{api_version}/ad/uploadAssets'

    headers = {
        'accept': 'application/json',
        'Access-Token': session.access_token
    }

    data = {
        'adAccountId': ad_account_id
    }

    files = {
        'asset': media
    }