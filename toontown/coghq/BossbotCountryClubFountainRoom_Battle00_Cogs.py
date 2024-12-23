from .SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 110200
CogParent2 = 110800
BattleCellId = 0
BattleCellId2 = 1
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)},
               BattleCellId2: {'parentEntId': CogParent2,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': 13 + random.randint(-2, 0),
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 10 + random.randint(-2, 1),
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 13 + random.randint(-2, 0),
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 15 + random.randint(-5, -1),
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent2,
  'boss': 0,
  'level': 13 + random.randint(-1, 1),
  'battleCell': BattleCellId2,
  'pos': Point3(-4, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent2,
  'boss': 0,
  'level': 17 + random.randint(-1, 2),
  'battleCell': BattleCellId2,
  'pos': Point3(0, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent2,
  'boss': 0,
  'suitName': 'bar',
  'level': 10 + random.randint(-2, 0),
  'battleCell': BattleCellId2,
  'pos': Point3(4, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
