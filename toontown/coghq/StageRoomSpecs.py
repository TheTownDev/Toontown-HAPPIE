from direct.showbase.PythonUtil import invertDict
from toontown.toonbase import ToontownGlobals
from toontown.coghq import NullCogs
from toontown.coghq import LawbotOfficeOilRoom_Battle00_Cogs
from toontown.coghq import LawbotOfficeOilRoom_Battle01_Cogs
from toontown.coghq import LawbotOfficeBoilerRoom_Battle00_Cogs
from toontown.coghq import LawbotOfficeBoilerRoom_Battle01_Cogs
from toontown.coghq import LawbotOfficeBoilerRoom_Trap00_Cogs
from toontown.coghq import LawbotOfficeLobby_Trap00_Cogs
from toontown.coghq import LawbotOfficeDiamondRoom_Trap00_Cogs
from toontown.coghq import LawbotOfficeDiamondRoom_Battle00_Cogs
from toontown.coghq import LawbotOfficeDiamondRoom_Battle01_Cogs
from toontown.coghq import LawbotOfficeGearRoom_Battle00_Cogs
from toontown.coghq import LawbotOfficeLavaRoomFoyer_Battle00_Cogs

from toontown.coghq import LawbotOfficeEntrance_Action00
from toontown.coghq import LawbotOfficeOilRoom_Battle00
from toontown.coghq import LawbotOfficeOilRoom_Battle01
from toontown.coghq import LawbotOfficeBoilerRoom_Security00
from toontown.coghq import LawbotOfficeBoilerRoom_Battle00
from toontown.coghq import LawbotOfficeBoilerRoom_Battle01
from toontown.coghq import LawbotOfficeGearRoom_Action00
from toontown.coghq import LawbotOfficeLobby_Action00
from toontown.coghq import LawbotOfficeGearRoom_Security00
from toontown.coghq import LawbotOfficeLobby_Trap00
from toontown.coghq import LawbotOfficeDiamondRoom_Security00
from toontown.coghq import LawbotOfficeDiamondRoom_Trap00
from toontown.coghq import LawbotOfficeGearRoom_Platform00
from toontown.coghq import LawbotOfficeLobby_Lights00
from toontown.coghq import LawbotOfficeBoilerRoom_Action01
from toontown.coghq import LawbotOfficeDiamondRoom_Action00
from toontown.coghq import LawbotOfficeDiamondRoom_Action01
from toontown.coghq import LawbotOfficeLobby_Action01
from toontown.coghq import LawbotOfficeDiamondRoom_Battle00
from toontown.coghq import LawbotOfficeDiamondRoom_Battle01
from toontown.coghq import LawbotOfficeGearRoom_Battle00
from toontown.coghq import LawbotOfficeLavaRoomFoyer_Battle00
from toontown.coghq import LawbotOfficeLobby_Battle00, LawbotOfficeLobby_Battle00_Cogs
from toontown.coghq import LawbotOfficeBookRoom_Battle00, LawbotOfficeBookRoom_Battle00_Cogs

from toontown.coghq.facility.lawbot.junior import tt_f_ara_dbr_action00
from toontown.coghq.facility.lawbot.junior import tt_f_ara_der_action00, tt_f_ara_der_action01, tt_f_ara_der_action02
from toontown.coghq.facility.lawbot.junior import tt_f_ara_ddr_action00, tt_f_ara_ddr_action01, tt_f_ara_ddr_action02, tt_f_ara_ddr_action04
from toontown.coghq.facility.lawbot.junior import tt_f_ara_delr_action00
from toontown.coghq.facility.lawbot.junior import tt_f_ara_dlr_action00, tt_f_ara_dlr_action01
from toontown.coghq.facility.lawbot.junior import tt_f_ara_dtr_action00, tt_f_ara_dtr_action01
from toontown.coghq.facility.lawbot.junior import tt_f_ara_dgr_action00, tt_f_ara_dgr_action01, tt_f_ara_dgr_action02, tt_f_ara_dgr_action04, tt_f_ara_dgr_action05

from toontown.coghq.facility.lawbot.junior import tt_f_ara_dbr_action00Cogs
from toontown.coghq.facility.lawbot.junior import tt_f_ara_der_action01Cogs, tt_f_ara_der_action02Cogs
from toontown.coghq.facility.lawbot.junior import tt_f_ara_ddr_action02Cogs, tt_f_ara_ddr_action04Cogs
from toontown.coghq.facility.lawbot.junior import tt_f_ara_dlr_action00Cogs
from toontown.coghq.facility.lawbot.junior import tt_f_ara_dtr_action00Cogs, tt_f_ara_dtr_action01Cogs
from toontown.coghq.facility.lawbot.junior import tt_f_ara_dgr_action04Cogs, tt_f_ara_dgr_action05Cogs
#JUNIOR WING ROOMS
JUNIOR_BOOK_ROOM = 200 # tt_f_ara_dbr_action00
JUNIOR_EVIDENCE_GOON_ROOM = 201 # tt_f_ara_der_action00
JUNIOR_EVIDENCE_DOOM_ROOM = 202 # tt_f_ara_der_action01
JUNIOR_EVIDENCE_SINGLE_ROOM = 203 # tt_f_ara_der_action02
JUNIOR_DIAMOND_STOMPER_ROOM = 204 # tt_f_ara_ddr_action00
JUNIOR_DIAMOND_GOON_ROOM = 205 # tt_f_ara_ddr_action01
JUNIOR_DIAMOND_SINGLE_ROOM = 206 # tt_f_ara_ddr_action02
JUNIOR_DIAMOND_DOOM_ROOM = 207 # tt_f_ara_ddr_action04
JUNIOR_ENTRANCE_ROOM = 208 # tt_f_ara_delr_action00
JUNIOR_TRAP_LOBBY_ROOM = 209 # tt_f_ara_dtr_action00
JUNIOR_TRAP_DIAMOND_ROOM = 210 # tt_f_ara_dtr_action01
JUNIOR_LOBBY_COGS = 211 # tt_f_ara_dlr_action00
JUNIOR_LOBBY_CAMERAS = 212 # tt_f_ara_dlr_action01
JUNIOR_BOX_GOON_ROOM = 213 # tt_f_ara_dgr_action00
JUNIOR_BOX_PLATFORM_ROOM = 214 # tt_f_ara_dgr_action01
JUNIOR_BOX_SECURITY_ROOM = 215 # tt_f_ara_dgr_action02
JUNIOR_BOX_SINGLE_ROOM = 216 # tt_f_ara_dgr_action04
JUNIOR_BOX_DOOM_ROOM = 217 # tt_f_ara_dgr_action05

LawbotStageSpecModules = {
    0: LawbotOfficeEntrance_Action00,
    1: LawbotOfficeOilRoom_Battle00,
    2: LawbotOfficeOilRoom_Battle01,
    3: LawbotOfficeBoilerRoom_Security00,
    4: LawbotOfficeBoilerRoom_Battle00,
    5: LawbotOfficeGearRoom_Action00,
    6: LawbotOfficeLobby_Action00,
    7: LawbotOfficeGearRoom_Security00,
    8: LawbotOfficeLobby_Trap00,
    9: LawbotOfficeDiamondRoom_Security00,
    10: LawbotOfficeDiamondRoom_Trap00,
    11: LawbotOfficeGearRoom_Platform00,
    12: LawbotOfficeLobby_Lights00,
    100: LawbotOfficeBoilerRoom_Action01,
    101: LawbotOfficeDiamondRoom_Action00,
    102: LawbotOfficeDiamondRoom_Action01,
    103: LawbotOfficeLobby_Action01,
    104: LawbotOfficeDiamondRoom_Battle00,
    105: LawbotOfficeGearRoom_Battle00,
    106: LawbotOfficeDiamondRoom_Battle01,
    107: LawbotOfficeBoilerRoom_Battle01,
    108: LawbotOfficeLavaRoomFoyer_Battle00,
    109: LawbotOfficeLobby_Battle00,
    110: LawbotOfficeBookRoom_Battle00,

    200: tt_f_ara_dbr_action00,
    201: tt_f_ara_der_action00,
    202: tt_f_ara_der_action01,
    203: tt_f_ara_der_action02,
    204: tt_f_ara_ddr_action00,
    205: tt_f_ara_ddr_action01,
    206: tt_f_ara_ddr_action02,
    207: tt_f_ara_ddr_action04,
    208: tt_f_ara_delr_action00,
    209: tt_f_ara_dtr_action00,
    210: tt_f_ara_dtr_action01,
    211: tt_f_ara_dlr_action00,
    212: tt_f_ara_dlr_action01,
    213: tt_f_ara_dgr_action00,
    214: tt_f_ara_dgr_action01,
    215: tt_f_ara_dgr_action02,
    216: tt_f_ara_dgr_action04,
    217: tt_f_ara_dgr_action05

}

# Ok don't freak out. What we are doing here is grabbing the name of the module that we imported.
# The problem is that it will include the path to this python module meaning we get: toontown.coghq.<MODULE_NAME>
# All we are doing is splitting the string by the periods, and grabbing the last section of it.
# For example, 'toontown.coghq.LawbotOfficeDiamondRoom_Trap00' becomes 'LawbotOfficeDiamondRoom_Trap00'
LawbotStageRoomId2RoomName = {_id: module.__name__.split('.')[-1] for _id, module in LawbotStageSpecModules.items()}

CogSpecModules = {
    'LawbotOfficeOilRoom_Battle00': LawbotOfficeOilRoom_Battle00_Cogs,
    'LawbotOfficeOilRoom_Battle01': LawbotOfficeOilRoom_Battle01_Cogs,
    'LawbotOfficeBoilerRoom_Battle00': LawbotOfficeBoilerRoom_Battle00_Cogs,
    'LawbotOfficeBoilerRoom_Trap00': LawbotOfficeBoilerRoom_Trap00_Cogs,
    'LawbotOfficeLobby_Trap00': LawbotOfficeLobby_Trap00_Cogs,
    'LawbotOfficeDiamondRoom_Trap00': LawbotOfficeDiamondRoom_Trap00_Cogs,
    'LawbotOfficeDiamondRoom_Battle00': LawbotOfficeDiamondRoom_Battle00_Cogs,
    'LawbotOfficeGearRoom_Battle00': LawbotOfficeGearRoom_Battle00_Cogs,
    'LawbotOfficeDiamondRoom_Battle01': LawbotOfficeDiamondRoom_Battle01_Cogs,
    'LawbotOfficeBoilerRoom_Battle01': LawbotOfficeBoilerRoom_Battle01_Cogs,
    'LawbotOfficeLavaRoomFoyer_Battle00': LawbotOfficeLavaRoomFoyer_Battle00_Cogs,
    'LawbotOfficeLobby_Battle00': LawbotOfficeLobby_Battle00_Cogs,
    'LawbotOfficeBookRoom_Battle00': LawbotOfficeBookRoom_Battle00_Cogs,
    'tt_f_ara_dbr_action00': tt_f_ara_dbr_action00Cogs,
    'tt_f_ara_der_action01': tt_f_ara_der_action01Cogs,
    'tt_f_ara_der_action02': tt_f_ara_der_action02Cogs,
    'tt_f_ara_ddr_action02': tt_f_ara_ddr_action02Cogs,
    'tt_f_ara_ddr_action04': tt_f_ara_ddr_action04Cogs,
    'tt_f_ara_dtr_action00': tt_f_ara_dtr_action00Cogs,
    'tt_f_ara_dtr_action01': tt_f_ara_dtr_action01Cogs,
    'tt_f_ara_dgr_action04': tt_f_ara_dgr_action04Cogs,
    'tt_f_ara_dgr_action05': tt_f_ara_dgr_action05Cogs

}


def getStageRoomSpecModule(roomId):
    return LawbotStageSpecModules[roomId]


def getCogSpecModule(roomId):
    roomName = LawbotStageRoomId2RoomName[roomId]
    return CogSpecModules.get(roomName, NullCogs)


def getNumBattles(roomId):
    return roomId2numBattles[roomId]


CashbotStageRoomName2RoomId = invertDict(LawbotStageRoomId2RoomName)
CashbotStageEntranceIDs = (0,)
CashbotStageMiddleRoomIDs = (1,)
CashbotStageFinalRoomIDs = (2,)
CashbotStageConnectorRooms = ('phase_11/models/lawbotHQ/LB_connector_7cubeL2', 'phase_11/models/lawbotHQ/LB_connector_7cubeLR')


roomId2numBattles = {}
for roomName, roomId in list(CashbotStageRoomName2RoomId.items()):
    if roomName not in CogSpecModules:
        roomId2numBattles[roomId] = 0
    else:
        cogSpecModule = CogSpecModules[roomName]
        roomId2numBattles[roomId] = len(cogSpecModule.BattleCells)

roomId2numCogs = {}
for roomName, roomId in list(CashbotStageRoomName2RoomId.items()):
    if roomName not in CogSpecModules:
        roomId2numCogs[roomId] = 0
    else:
        cogSpecModule = CogSpecModules[roomName]
        roomId2numCogs[roomId] = len(cogSpecModule.CogData)

roomId2numCogLevels = {}
for roomName, roomId in list(CashbotStageRoomName2RoomId.items()):
    if roomName not in CogSpecModules:
        roomId2numCogLevels[roomId] = 0
    else:
        cogSpecModule = CogSpecModules[roomName]
        levels = 0
        for cogData in cogSpecModule.CogData:
            levels += cogData['level']

        roomId2numCogLevels[roomId] = levels

roomId2numMeritCogLevels = {}
for roomName, roomId in list(CashbotStageRoomName2RoomId.items()):
    if roomName not in CogSpecModules or roomId in (8, 10):
        roomId2numMeritCogLevels[roomId] = 0
    else:
        cogSpecModule = CogSpecModules[roomName]
        levels = 0
        for cogData in cogSpecModule.CogData:
            levels += cogData['level']

        roomId2numMeritCogLevels[roomId] = levels

middleRoomId2numBattles = {}
for roomId in CashbotStageMiddleRoomIDs:
    middleRoomId2numBattles[roomId] = roomId2numBattles[roomId]
