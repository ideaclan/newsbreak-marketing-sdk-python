from enum import Enum

class Status(str, Enum):
    """
    This for status of an object
    """
    ON = 'ON'
    OFF = 'OFF'