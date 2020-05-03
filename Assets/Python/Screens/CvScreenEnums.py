## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005

# Enum for screens...

from CvPythonExtensions import CivilopediaPageTypes

DOMESTIC_ADVISOR = 0
REWARD_SCREEN = 1
DAWN_OF_MAN = 2
TECH_CHOOSER = 3
FOREIGN_ADVISOR = 4
FINANCE_ADVISOR = 5
WONDER_MOVIE_SCREEN = 6
RELIGION_SCREEN = 7
INTRO_MOVIE_SCREEN = 8
CIVICS_SCREEN = 9
DIPLOMACY_SCREEN = 10
OPTIONS_SCREEN = 11
TECH_SPLASH = 12
REPLAY_SCREEN = 13
MILITARY_ADVISOR = 14
VICTORY_SCREEN = 15
TOP_CIVS = 16
TUTORIAL_SCREEN = 17
INFO_SCREEN = 18
ERA_MOVIE_SCREEN = 19
ADVISOR_SCREEN = 20
HALL_OF_FAME = 21
DAN_QUAYLE_SCREEN = 22
WORLDBUILDER_SCREEN = 23
WORLDBUILDER_DIPLOMACY_SCREEN = 24
VICTORY_MOVIE_SCREEN = 25
UN_SCREEN = 26
ESPIONAGE_ADVISOR = 27
SPACE_SHIP_SCREEN = 28
CORPORATION_SCREEN = 29

MAIN_INTERFACE = 99
DEBUG_INFO_SCREEN = 100

# Civilopedia Pages start at 200
PEDIA_START = 200
PEDIA_MAIN = 199#CivilopediaPageTypes.CIVILOPEDIA_PAGE_MAIN + PEDIA_START
PEDIA_TECH = CivilopediaPageTypes.CIVILOPEDIA_PAGE_TECH + PEDIA_START
PEDIA_UNIT = CivilopediaPageTypes.CIVILOPEDIA_PAGE_UNIT + PEDIA_START
PEDIA_BUILDING = CivilopediaPageTypes.CIVILOPEDIA_PAGE_BUILDING + PEDIA_START
PEDIA_TERRAIN = CivilopediaPageTypes.CIVILOPEDIA_PAGE_TERRAIN + PEDIA_START
PEDIA_FEATURE = CivilopediaPageTypes.CIVILOPEDIA_PAGE_FEATURE + PEDIA_START
PEDIA_BONUS = CivilopediaPageTypes.CIVILOPEDIA_PAGE_BONUS + PEDIA_START
PEDIA_IMPROVEMENT = CivilopediaPageTypes.CIVILOPEDIA_PAGE_IMPROVEMENT + PEDIA_START
PEDIA_SPECIALIST = CivilopediaPageTypes.CIVILOPEDIA_PAGE_SPECIALIST + PEDIA_START
PEDIA_PROMOTION = CivilopediaPageTypes.CIVILOPEDIA_PAGE_PROMOTION + PEDIA_START
PEDIA_UNIT_CHART = CivilopediaPageTypes.CIVILOPEDIA_PAGE_UNIT_GROUP + PEDIA_START
PEDIA_CIVILIZATION = CivilopediaPageTypes.CIVILOPEDIA_PAGE_CIV + PEDIA_START
PEDIA_LEADER = CivilopediaPageTypes.CIVILOPEDIA_PAGE_LEADER + PEDIA_START
PEDIA_RELIGION = CivilopediaPageTypes.CIVILOPEDIA_PAGE_RELIGION + PEDIA_START
PEDIA_CORPORATION = CivilopediaPageTypes.CIVILOPEDIA_PAGE_CORPORATION + PEDIA_START
PEDIA_CIVIC = CivilopediaPageTypes.CIVILOPEDIA_PAGE_CIVIC + PEDIA_START
PEDIA_PROJECT = CivilopediaPageTypes.CIVILOPEDIA_PAGE_PROJECT + PEDIA_START
PEDIA_CONCEPT = CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT + PEDIA_START
PEDIA_CONCEPT_NEW = CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT_NEW + PEDIA_START
PEDIA_HINTS = CivilopediaPageTypes.CIVILOPEDIA_PAGE_HINTS + PEDIA_START
PEDIA_HISTORY = PEDIA_HINTS+1#CivilopediaPageTypes.CIVILOPEDIA_PAGE_HISTORY + PEDIA_START

# Updater Mod
MODUPDATER_SCREEN = 2000
# Updater Mod END
