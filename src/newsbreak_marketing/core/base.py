class APISession:
    """This class is to create a session object that it use to make Campaign, Ad and AdSet including uploading assets.

    ### Class Attributes:
        - access_token (str): Access token given by Newsbreak
        - api_version (str): API version want to use Default is `v1`
    """
    access_token: str
    api_version: str = 'v1'
    
    def __init__(self, access_token:str|None = None, api_version:str|None = None):
        if access_token:
            APISession.access_token = access_token
        if api_version:
            APISession.api_version = api_version