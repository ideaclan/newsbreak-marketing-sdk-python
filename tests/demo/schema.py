from enum import Enum
import strawberry

@strawberry.enum
class Status(str, Enum):
    """
    This for status of an object
    """
    ON = 'ON'
    OFF = 'OFF'