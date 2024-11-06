from .SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 10001
BattlePlace1 = 10001
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': 13,
  'battleCell': BattleCellId,
  'pos': Point3(-8, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 11,
  'battleCell': BattleCellId,
  'pos': Point3(-3, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 15,
  'battleCell': BattleCellId,
  'pos': Point3(3, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 11,
  'battleCell': BattleCellId,
  'pos': Point3(8, 4, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
