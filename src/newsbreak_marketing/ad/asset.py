import mimetypes
import os
import io

from newsbreak_marketing.utils.api_request import request

async def upload(session, ad_account_id:int|str, media:io.IOBase, api_version:str|None = None):
    """
    Uploads an asset to the platform.

    ### Args:
        - session (APISession): An instance of APISession.
        - ad_account_id (int|str): The ad account id.
        - media (io.IOBase): A file-like object to upload.
        - api_version (str|None): The API version to use. If not given use the one in the session object.

    ### Returns:
        - str: The URL of the uploaded asset.
    """
    api_version = api_version or session.api_version
    url = f'{api_version}/ad/uploadAssets'

    headers = {
        'accept': 'application/json',
        'Access-Token': session.access_token
    }

    data = {
        'adAccountId': ad_account_id
    }

    filename = os.path.basename(media.name) #type: ignore
    mime_type, _ = mimetypes.guess_type(filename)
    mime_type = mime_type or "application/octet-stream"

    files = {
        'asset': (filename, media, mime_type)
    }

    data = await request('POST', url, headers, data=data, files=files)

    return data['assetUrl']