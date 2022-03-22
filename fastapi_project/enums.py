from enum import Enum


class Races(str, Enum):
    TERRAN = 'terran'
    ZERG = 'zerg'
    PROTOSS = 'protoss'


class BuildTypes(str, Enum):
    MACRO = 'macro'
    CHEESE = 'cheese'
    ALL_IN = 'all-in'
