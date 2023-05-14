from enum import Enum


class UpdateType(Enum):
    ALL = "all"
    UNKNOWN = "unknown"

    def __str__(self):
        return self.value

    @staticmethod
    def from_string(s):
        try:
            return UpdateType[s.upper()]
        except KeyError:
            raise ValueError()
