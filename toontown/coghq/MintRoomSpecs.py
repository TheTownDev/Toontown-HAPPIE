from direct.showbase.PythonUtil import invertDict
from toontown.toonbase import ToontownGlobals
from toontown.coghq import NullCogs
from toontown.coghq import CashbotMintBoilerRoom_Battle00_Cogs
from toontown.coghq import CashbotMintBoilerRoom_Battle01_Cogs
from toontown.coghq import CashbotMintControlRoom_Battle00_Cogs
from toontown.coghq import CashbotMintDuctRoom_Battle00_Cogs
from toontown.coghq import CashbotMintDuctRoom_Battle01_Cogs
from toontown.coghq import CashbotMintGearRoom_Battle00_Cogs
from toontown.coghq import CashbotMintGearRoom_Battle01_Cogs
from toontown.coghq import CashbotMintLavaRoomFoyer_Battle00_Cogs
from toontown.coghq import CashbotMintLavaRoomFoyer_Battle01_Cogs
from toontown.coghq import CashbotMintLobby_Battle00_Cogs
from toontown.coghq import CashbotMintLobby_Battle01_Cogs
from toontown.coghq import CashbotMintOilRoom_Battle00_Cogs
from toontown.coghq import CashbotMintPaintMixerReward_Battle00_Cogs
from toontown.coghq import CashbotMintPipeRoom_Battle00_Cogs
from toontown.coghq import CashbotMintPipeRoom_Battle01_Cogs

from toontown.coghq import CashbotMintEntrance_Action00
from toontown.coghq import CashbotMintBoilerRoom_Action00
from toontown.coghq import CashbotMintBoilerRoom_Battle00
from toontown.coghq import CashbotMintDuctRoom_Action00
from toontown.coghq import CashbotMintDuctRoom_Battle00
from toontown.coghq import CashbotMintGearRoom_Action00
from toontown.coghq import CashbotMintGearRoom_Battle00
from toontown.coghq import CashbotMintLavaRoomFoyer_Action00
from toontown.coghq import CashbotMintLavaRoomFoyer_Action01
from toontown.coghq import CashbotMintLavaRoomFoyer_Battle00
from toontown.coghq import CashbotMintLavaRoom_Action00
from toontown.coghq import CashbotMintLobby_Action00
from toontown.coghq import CashbotMintLobby_Battle00
from toontown.coghq import CashbotMintPaintMixer_Action00
from toontown.coghq import CashbotMintPipeRoom_Action00
from toontown.coghq import CashbotMintPipeRoom_Battle00
from toontown.coghq import CashbotMintStomperAlley_Action00
from toontown.coghq import CashbotMintBoilerRoom_Battle01
from toontown.coghq import CashbotMintControlRoom_Battle00
from toontown.coghq import CashbotMintDuctRoom_Battle01
from toontown.coghq import CashbotMintGearRoom_Battle01
from toontown.coghq import CashbotMintLavaRoomFoyer_Battle01
from toontown.coghq import CashbotMintOilRoom_Battle00
from toontown.coghq import CashbotMintLobby_Battle01
from toontown.coghq import CashbotMintPaintMixerReward_Battle00
from toontown.coghq import CashbotMintPipeRoom_Battle01

from toontown.coghq.facility.cashbot.coin import tt_f_ara_mer_action00, tt_f_ara_bcr_action00, tt_f_ara_mmz_action00, tt_f_ara_mlr_action00, tt_f_ara_mgr_action00, tt_f_ara_mgr_action01
from toontown.coghq.facility.cashbot.coin import tt_f_ara_bcr_action00Cogs
from toontown.coghq.facility.cashbot.coin import tt_f_ara_mvr_action00, tt_f_ara_mvr_action00Cogs
from toontown.coghq.facility.cashbot.coin import tt_f_ara_mlr_action01, tt_f_ara_mlr_action01Cogs
from toontown.coghq.facility.cashbot.coin import tt_f_ara_mpr_action01, tt_f_ara_mpr_action00Cogs, tt_f_ara_mpr_action01Cogs
from toontown.coghq.facility.cashbot.coin import ttr_f_ara_mllr_action00, ttr_f_ara_mllr_action01, ttr_f_ara_mllr_action02

from toontown.coghq.facility.cashbot.coin.auditor_rooms import tt_fb_ara_mvr_action00
from toontown.coghq.facility.cashbot.coin.auditor_rooms import tt_fb_ara_mvr_action00Cogs

def getMintRoomSpecModule(roomId):
    return CashbotMintSpecModules[roomId]


def getCogSpecModule(roomId):
    roomName = CashbotMintRoomId2RoomName[roomId]
    return CogSpecModules.get(roomName, NullCogs)


def getNumBattles(roomId):
    return roomId2numBattles[roomId]

CashbotMintSpecModules = {
    0: tt_f_ara_mer_action00,
    1: CashbotMintBoilerRoom_Action00,
    2: CashbotMintBoilerRoom_Battle00,
    3: CashbotMintDuctRoom_Action00,
    4: CashbotMintDuctRoom_Battle00,
    5: CashbotMintGearRoom_Action00,
    6: CashbotMintGearRoom_Battle00,
    7: CashbotMintLavaRoomFoyer_Action00,
    8: CashbotMintLavaRoomFoyer_Action01,
    9: CashbotMintLavaRoomFoyer_Battle00,
    10: CashbotMintLavaRoom_Action00,
    11: CashbotMintLobby_Action00,
    12: CashbotMintLobby_Battle00,
    13: CashbotMintPaintMixer_Action00,
    14: CashbotMintPipeRoom_Action00,
    15: CashbotMintPipeRoom_Battle00,
    16: CashbotMintStomperAlley_Action00,
    17: CashbotMintBoilerRoom_Battle01,
    18: CashbotMintControlRoom_Battle00,
    19: CashbotMintDuctRoom_Battle01,
    20: CashbotMintGearRoom_Battle01,
    21: CashbotMintLavaRoomFoyer_Battle01,
    22: CashbotMintOilRoom_Battle00,
    23: CashbotMintLobby_Battle01,
    24: CashbotMintPaintMixerReward_Battle00,
    25: CashbotMintPipeRoom_Battle01,
    100: tt_f_ara_bcr_action00,
    101: tt_f_ara_mvr_action00,
    102: tt_f_ara_mmz_action00,
    103: tt_f_ara_mlr_action00,
    104: tt_f_ara_mgr_action00,
    105: tt_f_ara_mlr_action01,
    106: tt_f_ara_mgr_action01,
    107: tt_f_ara_mpr_action01,
    108: tt_fb_ara_mvr_action00,
    109: ttr_f_ara_mllr_action00,
    110: ttr_f_ara_mllr_action01,
    111: ttr_f_ara_mllr_action02
}

# Ok don't freak out. What we are doing here is grabbing the name of the module that we imported.
# The problem is that it will include the path to this python module meaning we get: toontown.coghq.<MODULE_NAME>
# All we are doing is splitting the string by the periods, and grabbing the last section of it.
# For example, 'toontown.coghq.CashbotMintPipeRoom_Battle00' becomes 'CashbotMintPipeRoom_Battle00'
CashbotMintRoomId2RoomName = {_id: module.__name__.split('.')[-1] for _id, module in CashbotMintSpecModules.items()}

CashbotMintRoomName2RoomId = invertDict(CashbotMintRoomId2RoomName)
CashbotMintEntranceIDs = (0,)
CashbotMintMiddleRoomIDs = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
CashbotMintFinalRoomIDs = (17, 18, 19, 20, 21, 22, 23, 24, 25)
CashbotMintConnectorRooms = ('phase_10/models/cashbotHQ/connector_7cubeL2', 'phase_10/models/cashbotHQ/connector_7cubeR2')

CogSpecModules = {
    'CashbotMintBoilerRoom_Battle00': CashbotMintBoilerRoom_Battle00_Cogs,
    'CashbotMintBoilerRoom_Battle01': CashbotMintBoilerRoom_Battle01_Cogs,
    'CashbotMintControlRoom_Battle00': CashbotMintControlRoom_Battle00_Cogs,
    'CashbotMintDuctRoom_Battle00': CashbotMintDuctRoom_Battle00_Cogs,
    'CashbotMintDuctRoom_Battle01': CashbotMintDuctRoom_Battle01_Cogs,
    'CashbotMintGearRoom_Battle00': CashbotMintGearRoom_Battle00_Cogs,
    'CashbotMintGearRoom_Battle01': CashbotMintGearRoom_Battle01_Cogs,
    'CashbotMintLavaRoomFoyer_Battle00': CashbotMintLavaRoomFoyer_Battle00_Cogs,
    'CashbotMintLavaRoomFoyer_Battle01': CashbotMintLavaRoomFoyer_Battle01_Cogs,
    'CashbotMintLobby_Battle00': CashbotMintLobby_Battle00_Cogs,
    'CashbotMintLobby_Battle01': CashbotMintLobby_Battle01_Cogs,
    'CashbotMintOilRoom_Battle00': CashbotMintOilRoom_Battle00_Cogs,
    'CashbotMintPaintMixerReward_Battle00': CashbotMintPaintMixerReward_Battle00_Cogs,
    'CashbotMintPipeRoom_Battle00': CashbotMintPipeRoom_Battle00_Cogs,
    'CashbotMintPipeRoom_Battle01': CashbotMintPipeRoom_Battle01_Cogs,
    'tt_f_ara_bcr_action00': tt_f_ara_bcr_action00Cogs,
    'tt_f_ara_mvr_action00': tt_f_ara_mvr_action00Cogs,
    'tt_f_ara_mlr_action01': tt_f_ara_mlr_action01Cogs,
    'tt_f_ara_mpr_action01': tt_f_ara_mpr_action01Cogs,
    'tt_fb_ara_mvr_action00': tt_fb_ara_mvr_action00Cogs
}

roomId2numBattles = {}

for roomName, roomId in CashbotMintRoomName2RoomId.items():
    if roomName not in CogSpecModules:
        roomId2numBattles[roomId] = 0
    else:
        cogSpecModule = CogSpecModules[roomName]
        roomId2numBattles[roomId] = len(cogSpecModule.BattleCells)

roomId2numBattles[CashbotMintRoomName2RoomId['CashbotMintBoilerRoom_Battle00']] = 3
roomId2numBattles[CashbotMintRoomName2RoomId['CashbotMintPipeRoom_Battle00']] = 2

middleRoomId2numBattles = {}
for roomId in CashbotMintMiddleRoomIDs:
    middleRoomId2numBattles[roomId] = roomId2numBattles[roomId]
