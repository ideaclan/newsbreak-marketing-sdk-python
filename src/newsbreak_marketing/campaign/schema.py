from enum import Enum

class CampaignObjective(str,Enum):
    """
    Objectives of a campaign
    """
    WEB_CONVERSION = "WEB_CONVERSION"
    APP_CONVERSION = "APP_CONVERSION"
    REACH = "REACH"
    WEB_TRAFFIC = "WEB_TRAFFIC"
    APP_TRAFFIC = "APP_TRAFFIC"

class CampaignOnlineStatus(str,Enum):
    """
    Status of a campaign
    """
    WARNING = "WARNING"
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"
    DELETE = "DELETE"
    DELETED = "DELETED"