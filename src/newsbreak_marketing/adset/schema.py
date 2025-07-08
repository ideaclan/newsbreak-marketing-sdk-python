from enum import Enum
from pydantic import BaseModel, model_validator, field_validator
from typing import List, Optional

class AdSetBudgetType(str, Enum):
    DAILY = "DAILY"
    TOTAL = "TOTAL"

class AdSetBidType(str, Enum):
    CPM = "CPM"
    CPC = "CPC"
    TARGET_CPA = "TARGET_CPA"
    MAX_CONVERSION = "MAX_CONVERSION"

class AdSetDeliveryRate(str, Enum):
    EVENLY = "EVENLY"
    ASAP = "ASAP"

class Location(BaseModel):
    positive: Optional[List[str]] = ['all']
    negative: Optional[List[str]] = None

class GenderType(str, Enum):
    ND = 'notdisclosed'
    MALE = 'male'
    FEMALE = 'female'
    ALL = 'all'

class Gender(BaseModel):
    positive: Optional[List[GenderType]] = [GenderType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[GenderType])->List[GenderType]:
        if GenderType.ALL in value:
            return [GenderType.ALL]
        return value
    
class AgeType(str,Enum):
    ALL = 'all'
    A18_30 = '18-30'
    A31_44 = '31-44'
    A45_64 = '45-64'
    A65P = '65+'

class AgeGroup(BaseModel):
    positive: Optional[List[AgeType]] = [AgeType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[AgeType])->List[AgeType]:
        if AgeType.ALL in value:
            return [AgeType.ALL]
        return value

class LanguageType(str,Enum):
    ALL = 'all'
    EN_US = 'en_us'
    ES_US = 'es_us'

class Language(BaseModel):
    positive: Optional[List[LanguageType]] = [LanguageType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[LanguageType])->List[LanguageType]:
        if LanguageType.ALL in value:
            return [LanguageType.ALL]
        return value
    
class InterestType(str,Enum):
    ALL = 'all'

class Interest(BaseModel):
    positive: Optional[List[InterestType]] = [InterestType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[InterestType])->List[InterestType]:
        if InterestType.ALL in value:
            return [InterestType.ALL]
        return value
    
class OSType(str,Enum):
    ALL = 'all'

class OS(BaseModel):
    positive: Optional[List[OSType]] = [OSType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[OSType])->List[OSType]:
        if OSType.ALL in value:
            return [OSType.ALL]
        return value
class ManufacturerType(str,Enum):
    ALL = 'all'

class Manufacturer(BaseModel):
    positive: Optional[List[ManufacturerType]] = [ManufacturerType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[ManufacturerType])->List[ManufacturerType]:
        if ManufacturerType.ALL in value:
            return [ManufacturerType.ALL]
        return value
    
class CarrierType(str,Enum):
    ALL = 'all'

class Carrier(BaseModel):
    positive: Optional[List[CarrierType]] = [CarrierType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[CarrierType])->List[CarrierType]:
        if CarrierType.ALL in value:
            return [CarrierType.ALL]
        return value
    
class NetworkType(str,Enum):
    ALL = 'all'

class Network(BaseModel):
    positive: Optional[List[NetworkType]] = [NetworkType.ALL]

    @field_validator('positive')
    def enforce_all_only(value:List[NetworkType])->List[NetworkType]:
        if NetworkType.ALL in value:
            return [NetworkType.ALL]
        return value

class Targeting(BaseModel):
    location: Optional[Location] = Location()
    gender: Optional[Gender]= Gender()
    age_group: AgeGroup = AgeGroup()
    language: Language = Language()
    interest: Interest = Interest() 
    os: OS = OS()
    manufacturer: Manufacturer = Manufacturer()
    carrier: Carrier = Carrier()
    network: Network = Network()

class AdSetOnlineStatus(str, Enum):
    WARNING = "WARNING"
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"
    DELETE = "DELETE"
    READY = "READY"
    COMPLETED = "COMPLETED"