import mimetypes
import os
import io

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

    filename = os.path.basename(media.name)
    mime_type, _ = mimetypes.guess_type(filename)
    mime_type = mime_type or "application/octet-stream"

    files = {
        'asset': (filename, media, mime_type)
    }

    data = await request('POST', url, headers, data=data, files=files)

    return data['assetUrl']