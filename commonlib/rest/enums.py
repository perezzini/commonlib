from enum import Enum


class DBStatus(str, Enum):
    active = "active"
    inactive = "inactive"
