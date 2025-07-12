from enum import Enum
from pydantic import BaseModel, model_validator, field_validator
from typing import List

class AdSetBudgetType(str, Enum):
    """
    Budget Types of AdSet
    """
    DAILY = "DAILY"
    TOTAL = "TOTAL"

class AdSetBidType(str, Enum):
    """
    Types of Bid on AdSet
    """
    CPM = "CPM"
    CPC = "CPC"
    TARGET_CPA = "TARGET_CPA"
    MAX_CONVERSION = "MAX_CONVERSION"

class AdSetDeliveryRate(str, Enum):
    """
    Types of Delivery Rate
    """
    EVENLY = "EVENLY"
    ASAP = "ASAP"

class Location(BaseModel):
    """
    For Selecting Location to include
    """
    positive: List[str] = ['all']
    negative: List[str] = []

class GenderType(str, Enum):
    """
    Types of Genders
    """
    ND = 'notdisclosed'
    MALE = 'male'
    FEMALE = 'female'
    ALL = 'all'

class Gender(BaseModel):
    """
    For Selecting Gender to include
    """
    positive: List[GenderType] = [GenderType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[GenderType])->List[GenderType]: #type: ignore
        if GenderType.ALL in value:
            return [GenderType.ALL]
        return value
    
class AgeType(str,Enum):
    """
    Types of Age Groups
    """
    ALL = 'all'
    A18_30 = '18-30'
    A31_44 = '31-44'
    A45_64 = '45-64'
    A65P = '65+'

class AgeGroup(BaseModel):
    """
    For Selecting Age Group to include
    """
    positive: List[AgeType] = [AgeType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[AgeType])->List[AgeType]: #type: ignore
        if AgeType.ALL in value:
            return [AgeType.ALL]
        return value

class LanguageType(str,Enum):
    """
    Types of Languages
    """
    ALL = 'all'
    EN_US = 'en_us'
    ES_US = 'es_us'

class Language(BaseModel):
    """
    For Selecting Language to include
    """
    positive: List[LanguageType] = [LanguageType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[LanguageType])->List[LanguageType]: #type: ignore
        if LanguageType.ALL in value:
            return [LanguageType.ALL]
        return value
    
class InterestType(str,Enum):
    """
    Types of Interests
    """
    ALL = 'all'

class Interest(BaseModel):
    """
    For Selecting Interest to include
    """
    positive: List[InterestType] = [InterestType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[InterestType])->List[InterestType]: #type: ignore
        if InterestType.ALL in value:
            return [InterestType.ALL]
        return value
    
class OSType(str,Enum):
    """
    Types of OS
    """
    ALL = 'all'

class OS(BaseModel):
    """
    For Selecting OS to include
    """
    positive: List[OSType] = [OSType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[OSType])->List[OSType]: #type: ignore
        if OSType.ALL in value:
            return [OSType.ALL]
        return value
class ManufacturerType(str,Enum):
    """
    Types of Manufacturer
    """
    ALL = 'all'

class Manufacturer(BaseModel):
    """
    For Selecting Manufacturer to include
    """
    positive: List[ManufacturerType] = [ManufacturerType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[ManufacturerType])->List[ManufacturerType]: #type: ignore
        if ManufacturerType.ALL in value:
            return [ManufacturerType.ALL]
        return value
    
class CarrierType(str,Enum):
    """
    Type of carrier
    """
    ALL = 'all'

class Carrier(BaseModel):
    """
    For selecting carrier to include
    """
    positive: List[CarrierType] = [CarrierType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[CarrierType])->List[CarrierType]: #type: ignore
        if CarrierType.ALL in value:
            return [CarrierType.ALL]
        return value
    
class NetworkType(str,Enum):
    """
    Type of Network
    """
    ALL = 'all'

class Network(BaseModel):
    """
    For Selecting Network to include
    """
    positive: List[NetworkType] = [NetworkType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[NetworkType])->List[NetworkType]: #type: ignore
        if NetworkType.ALL in value:
            return [NetworkType.ALL]
        return value

class Targeting(BaseModel):
    """
    Targeting for an ad set

    #### By Default All will be included
    """
    location: Location = Location()
    gender: Gender = Gender()
    age_group: AgeGroup = AgeGroup()
    language: Language = Language()
    interest: Interest = Interest() 
    os: OS = OS()
    manufacturer: Manufacturer = Manufacturer()
    carrier: Carrier = Carrier()
    network: Network = Network()

class AdSetOnlineStatus(str, Enum):
    """
    Online status of an ad set
    """
    WARNING = "WARNING"
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"
    DELETE = "DELETE"
    READY = "READY"
    COMPLETED = "COMPLETED"