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
    A18_36 = '18-30'
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



class Targeting(BaseModel):
    location: Optional[Location] = Location()
    gender: Optional[Gender]= Gender()
    age_group = ...
    language = ...
    interest = ...
    os = ...
    manufacturer = ...
    carrier = ...
    network = ...



    