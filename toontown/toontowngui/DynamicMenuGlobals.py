from direct.gui import DirectGuiGlobals as DGG
from toontown.toonbase import TTLocalizer as TTL

DM_OBJ_PANEL = 'panel'
DM_OBJ_TEXT = 'text'
DM_OBJ_BUTTON = 'button'

SmoothTime = 0.2

ButtonImageScale = (0.7, 1, 1)
ButtonTextScale = 0.052
ButtonTextPos = (0, -0.02)

SpecialArgs = ['type', 'parent', 'command']

TYPE_BASE = 0
TYPE_QUICK_MENU = 1

MenuData = {
    TYPE_BASE: {
        1: {'type': DM_OBJ_PANEL}
    },
    TYPE_QUICK_MENU: {
        # Main panel
        1: {'type': DM_OBJ_PANEL,
            'sortOrder': DGG.NO_FADE_SORT_INDEX,
            'image_color': (0.2, 0.2, 0.4, 0.5),
            'image_scale': (1.75, 1, 0.5),
            'pos': (0, 0, -0.7)},
        # More categories at bottom
        2: {'type': DM_OBJ_BUTTON,
            'text': 'Places',
            'command': ['category', 2],
            'pos': (-0.7, 0, -0.125),
            'parent': 15},
        14002: {'type': DM_OBJ_BUTTON,
            'text': 'Battle',
            'command': ['category', 3],
            'pos': (-0.38, 0, -0.125),
            'parent': 15},
        # Back and exit, top right
        3: {'type': DM_OBJ_BUTTON,
            'text': 'Back',
            'command': ['category', 1],
            'image_scale': (0.3, 1, 1),
            'parent': 12},
        4: {'type': DM_OBJ_BUTTON,
            'text': 'Exit',
            'command': ['category', 0],
            'image_scale': (0.3, 1, 1),
            'parent': 12},
        # Shtickerbook button
        5: {'type': DM_OBJ_BUTTON,
            'text': 'Quick Menu',
            'command': ['category', 1],
            'pos': (-0.4, 0, 0.075),
            'parent': base.a2dBottomRight},
        # Main 5 commands
        6: {'type': DM_OBJ_BUTTON,
            'text': 'Oobe',
            'command': ['messenger', ['magicWord', ['~oobe']]],
            'pos': (-0.7, 0, 0),
            'parent': 11},
        7: {'type': DM_OBJ_BUTTON,
            'text': 'Run',
            'command': ['messenger', ['magicWord', ['~run']]],
            'pos': (-0.4, 0, 0),
            'parent': 11},
        8: {'type': DM_OBJ_BUTTON,
            'text': '-1 Gags',
            'command': ['messenger', ['magicWord', ['~unlimitedgags']]],
            'pos': (-0.1, 0, 0),
            'parent': 11},
        9: {'type': DM_OBJ_BUTTON,
            'text': 'Instakill',
            'command': ['messenger', ['magicWord', ['~instakill']]],
            'pos': (0.2, 0, 0),
            'parent': 11},
        10: {'type': DM_OBJ_BUTTON,
            'text': 'Immortal',
            'command': ['messenger', ['magicWord', ['~immortal']]],
            'pos': (0.5, 0, 0),
            'parent': 11},
        # Houses main 5 command buttons
        11: {'type': DM_OBJ_PANEL,
             'image': None,
             'pos': (0.05, 0, 0.175),
             'parent': 14},
        1400: {'type': DM_OBJ_PANEL,
             'image': None,
             'pos': (0.05, 0, 0.175),
             'parent': 14},
        # Houses all things of category 2
        1401: {'type': DM_OBJ_PANEL,
             'image': None,
             'parent': 1400},
        # Houses back and exit
        12: {'type': DM_OBJ_PANEL,
             'image': None,
             'pos': (0.8, 0, 0.175),
             'parent': 1},
        # Other categories label
        13: {'type': DM_OBJ_TEXT,
             'pos': (0, 0, 0),
             'text': 'Other Categories',
             'text_fg': (1, 1, 1, 1),
             'parent': 14},
        # Houses all things of category 1
        14: {'type': DM_OBJ_PANEL,
             'image': None,
             'parent': 1},
        # Houses all other categories as part of category 1
        15: {'type': DM_OBJ_PANEL,
             'image': None,
             'parent': 14},
        # Houses all things of places category
        16: {'type': DM_OBJ_PANEL,
             'image': None,
             'parent': 1},
        # Places label
        17: {'type': DM_OBJ_TEXT,
             'pos': (0, 0, 0.15),
             'text': 'Places',
             'text_fg': (1, 1, 1, 1),
             'parent': 16},
        # Houses all top row place buttons as part of category 2
        18: {'type': DM_OBJ_PANEL,
             'image': None,
             'pos': (0.025, 0, 0.05),
             'parent': 16},
        # Plcae buttons
        19: {'type': DM_OBJ_BUTTON,
            'text': 'TTC',
            'command': ['messenger', ['magicWord', ['~tp ttc']]],
            'pos': (-0.7, 0, 0),
            'parent': 18},
        20: {'type': DM_OBJ_BUTTON,
            'text': "DD",
            'command': ['messenger', ['magicWord', ['~tp dd']]],
            'pos': (-0.4, 0, 0),
            'parent': 18},
        21: {'type': DM_OBJ_BUTTON,
            'text': 'DG',
            'command': ['messenger', ['magicWord', ['~tp dg']]],
            'pos': (-0.1, 0, 0),
            'parent': 18},
        22: {'type': DM_OBJ_BUTTON,
            'text': "MML",
            'command': ['messenger', ['magicWord', ['~tp mml']]],
            'pos': (0.2, 0, 0),
            'parent': 18},
        23: {'type': DM_OBJ_BUTTON,
            'text': "TB",
            'command': ['messenger', ['magicWord', ['~tp tb']]],
            'pos': (0.5, 0, 0),
            'parent': 18},
        # Row two buttons
        24: {'type': DM_OBJ_BUTTON,
            'text': 'DDL',
            'command': ['messenger', ['magicWord', ['~tp ddl']]],
            'pos': (-0.7, 0, 0),
            'parent': 29},
        25: {'type': DM_OBJ_BUTTON,
            'text': "SBHQ",
            'command': ['messenger', ['magicWord', ['~tp sbhq']]],
            'pos': (-0.4, 0, 0),
            'parent': 29},
        26: {'type': DM_OBJ_BUTTON,
            'text': 'CBHQ',
            'command': ['messenger', ['magicWord', ['~tp cbhq']]],
            'pos': (-0.1, 0, 0),
            'parent': 29},
        27: {'type': DM_OBJ_BUTTON,
            'text': "LBHQ",
            'command': ['messenger', ['magicWord', ['~tp lbhq']]],
            'pos': (0.2, 0, 0),
            'parent': 29},
        28: {'type': DM_OBJ_BUTTON,
            'text': "BBHQ",
            'command': ['messenger', ['magicWord', ['~tp bbhq']]],
            'pos': (0.5, 0, 0),
            'parent': 29},
        # Houses row two buttons
        29: {'type': DM_OBJ_PANEL,
             'image': None,
             'pos': (0, 0, -0.1),
             'parent': 18},
        # Houses row three buttons
        30: {'type': DM_OBJ_PANEL,
             'image': None,
             'pos': (0, 0, -0.1),
             'parent': 29},
        # Row three buttons
        31: {'type': DM_OBJ_BUTTON,
            'text': 'Acorn Acres',
            'command': ['messenger', ['magicWord', ['~tp oz']]],
            'pos': (-0.7, 0, 0),
            'parent': 30},
        32: {'type': DM_OBJ_BUTTON,
            'text': "Speedway",
            'command': ['messenger', ['magicWord', ['~tp gs']]],
            'pos': (-0.4, 0, 0),
            'parent': 30},
        33: {'type': DM_OBJ_BUTTON,
            'text': 'Golf Zone',
            'command': ['messenger', ['magicWord', ['~tp gz']]],
            'pos': (-0.1, 0, 0),
            'parent': 30},
        34: {'type': DM_OBJ_BUTTON,
            'text': "Fact. Exterior",
            'command': ['messenger', ['magicWord', ['~tp factory']]],
            'pos': (0.2, 0, 0),
            'parent': 30},
        # 35: {'type': DM_OBJ_BUTTON,
        #     'text': "DA Lobby",
        #     'command': ['messenger', ['magicWord', ['~tp officea']]],
        #     'pos': (0.5, 0, 0),
        #     'parent': 30},
        # Underneath main 5 command buttons
        36: {'type': DM_OBJ_BUTTON,
            'text': 'Skip Mov.',
            'command': ['messenger', ['magicWord', ['~skipmovie']]],
            'pos': (-0.7, 0, -0.1),
            'parent': 11},
        # Categories
        'menu_category_0': {1: {'wantShow': False},
                            5: {'wantShow': True}},
        'menu_category_1': {1: {'wantShow': True},
                            3: {'wantShow': False},
                            4: {'wantShow': True,
                                'pos': (0, 0, 0)},
                            5: {'wantShow': False},
                            14: {'wantShow': True},
                            16: {'wantShow': False}},
        'menu_category_2': {3: {'wantShow': True},
                            4: {'pos': (0, 0, -0.11)},
                            14: {'wantShow': False},
                            16: {'wantShow': True}},
        'menu_category_3': {3: {'wantShow': True},
                            4: {'pos': (0, 0, -0.11)},
                            14: {'wantShow': False},
                            16: {'wantShow': False},
                            1400: {'wantShow': True},
                            1401: {'wantShow': True}},
    }
}