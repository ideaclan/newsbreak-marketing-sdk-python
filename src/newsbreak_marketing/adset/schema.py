from enum import Enum

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