from .ElevatorConstants import *

# floor and suit information for all suit buildings, organized by each
# level of suit that originally took over the building (minus 1), used
# to determine how many and what level of suits to create for the suit
# interiors
#
#    1  number of floors for this level building
#    2  suit level range, excluding the boss
#    3  boss level range
#    4  base level pool for total suits on each floor of the building
#    5  multipliers for item 4 for each floor of the building, generally
#       each consecutive floor increases the base range of the level pool
#    6 are they v2.0 cogs
#
SuitBuildingInfo = (
 # building difficulty 0 (suit level 1)
 ((1, 1), (1, 3), (4, 4), (8, 10), (1,)),  # 0
 # building difficulty 1 (suit level 2) 
 ((1, 2), (1, 3), (4, 4), (8, 10), (1, 1.2)),  # 1
 # building difficulty 2 (suit level 3)
 ((1, 3), (2, 4), (5, 5), (8, 10), (1, 1.3, 1.6)),  # 2
 # building difficulty 3 (suit level 4)
 ((2, 3), (4, 6), (7, 7), (8, 10), (1, 1.4, 1.8)),  # 3
 # building difficulty 4 (suit level 5)
 ((2, 4), (5, 8), (9, 9), (8, 10), (1, 1.6, 1.8, 2)),  # 4
 # building difficulty 5 (suit level 6)
 ((3, 4), (5, 9), (10, 10), (10, 12), (1, 1.6, 2, 2.4)),  # 5
 # building difficulty 6 (suit level 7)
 ((3, 5), (7, 10), (11, 11), (10, 14), (1, 1.6, 1.8, 2.2, 2.4)),  # 6
 # building difficulty 7 (suit level 8)
 ((4, 5), (7, 12), (13, 13), (12, 16), (1, 1.8, 2.4, 3, 3.2)),  # 7
 # building difficulty 8 (suit level 9)
 ((5, 5), (9, 14), (15, 15), (14, 20), (1.4, 1.8, 2.6, 3.4, 4)),  # 8
 # building difficulty 9 (suit level 10)
 ((5, 5), (9, 15), (16, 16), (14, 20), (2.0, 2.5, 3.0, 4.0, 6)),  # 9
 # building difficulty 10 (suit level 11)
 ((6, 6), (11, 17), (18, 18), (25, 30), (2.0, 2.5, 3.0, 4.0, 6, 6.5)),  # 10
 # building difficulty 11 (suit level 12)
 ((6, 6), (13, 19), (20, 20), (25, 30), (2.0, 2.5, 3.0, 4.0, 6, 6.5))  # 10
)
SuitBossInfo = (
 ((1, 1), (7, 14), (8, 8), (150, 150), (1, 1, 1, 1, 1)),  # 0 VP Round 1
 ((1, 1), (6, 13), (13, 14), (100, 100), (1, 1, 1, 1, 1)),  # 1 VP Round 2 Skelecogs
 ((1, 1), (6, 14), (13, 15), (120, 120), (1, 1, 1, 1, 1)),  # 2 CFO Round 1 NONSKELECOGS ONLY
 ((1, 1), (7, 16), (16, 16), (70, 70), (1, 1, 1, 1, 1)),  # 3 CFO Round 2 SKELECOGS ONLY
 ((1, 1), (8, 18), (18, 18), (100, 100), (1, 1, 1, 1, 1)),  # 4 CJ Round 1
 ((1, 1), (8, 20), (20, 20), (120, 120), (1, 1, 1, 1, 1), (0,)),  # 5 CEO Round 1
 ((1, 1), (1, 5), (5, 5), (33, 33), (1, 1, 1, 1, 1)),  # 6 Storm Sellbot Round 1
 ((1, 1), (4, 5), (5, 5), (50, 50), (1, 1, 1, 1, 1))  # 7 Storm Sellbot Round 2
)
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
SUIT_BLDG_INFO_IMMUNE = 6
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8
NUM_TOONS_TO_COGS_RATIO = {1: 1,
                           2: 0.35,
                           3: 0.45,
                           4: 0.6,
                           5: 0.65,
                           6: 0.75,
                           7: 0.9,
                           8: 1
                           }
