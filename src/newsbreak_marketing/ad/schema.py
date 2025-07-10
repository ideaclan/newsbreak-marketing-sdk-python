from pydantic import BaseModel
from enum import Enum
from typing import Optional

class CreativeType(str,Enum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    GIF = "GIF"

def to_camel(string: str) -> str:
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


class CreativeContent(BaseModel):
    headline: str
    asset_url: str
    height: Optional[int] = None
    width: Optional[int] = None
    cover_url: Optional[str] = None
    description: str
    call_to_action: str
    brand_name: str
    logo_url: Optional[str] = None
    click_through_url: str

    class Config:
        alias_generator = to_camel
        validate_by_name = True # <-- This allows keeping the original field name
        extra = "ignore"  # <-- This allows extra fields in input and ignores them

class Creative(BaseModel):
    type: CreativeType
    content: CreativeContent

    class Config:
        alias_generator = to_camel
        validate_by_name = True # <-- This allows keeping the original field name
        extra = "ignore"  # <-- This allows extra fields in input and ignores them

class AdAuditStatus(str,Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    