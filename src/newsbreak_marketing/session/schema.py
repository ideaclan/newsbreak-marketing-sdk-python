from pydantic import BaseModel
from typing import Optional

class SessionSchema(BaseModel):
    access_token:str
    api_version:Optional[str] = 'v1'