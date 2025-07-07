class APISession:
    access_token: str|None = None
    api_version: str|None = None
    
    def __init__(self, access_token:str|None = None, api_version:str|None = None):
        if access_token:
            APISession.access_token = access_token
        if api_version:
            APISession.api_version = api_version