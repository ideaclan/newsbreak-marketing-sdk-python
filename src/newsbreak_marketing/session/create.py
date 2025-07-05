from newsbreak_marketing.session.schema import SessionSchema

class Session:
    def __init__(self, access_token:str, api_version:str):
        session_schema = SessionSchema(access_token=access_token, api_version=api_version)

        self.access_token = session_schema.access_token
        self.api_version = session_schema.api_version