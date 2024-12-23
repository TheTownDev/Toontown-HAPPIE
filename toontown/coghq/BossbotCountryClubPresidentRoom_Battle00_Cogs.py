from .SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 110400
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 1,
  'suitName': 'bgh',
  'level': 20,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': 11,
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'suitName': 'cfn',
  'level': 15,
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'suitName': 'inv',
  'level': 14,
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 0}]
ReserveCogData = []
