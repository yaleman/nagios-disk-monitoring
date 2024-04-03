from enum import IntEnum


class NagiosResult(IntEnum):
    """result codes for Nagios checks"""

    OK = 0
    WARNING = 1
    CRITICAL = 2
    UNKNOWN = 3

    def __str__(self) -> str:
        return self.name
