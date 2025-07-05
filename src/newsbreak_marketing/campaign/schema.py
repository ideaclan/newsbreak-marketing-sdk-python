from enum import Enum

class CampaignObjective(str,Enum):
    WEB_CONVERSION = "WEB_CONVERSION"
    APP_CONVERSION = "APP_CONVERSION"
    REACH = "REACH"
    WEB_TRAFFIC = "WEB_TRAFFIC"
    APP_TRAFFIC = "APP_TRAFFIC"