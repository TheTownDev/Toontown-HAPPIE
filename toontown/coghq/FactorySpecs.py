from toontown.toonbase import ToontownGlobals
from toontown.coghq.facility.sellbot.scrap import tt_f_ara_fac_layout00
from toontown.coghq.facility.sellbot.scrap import tt_f_ara_fac_layout00Cogs
from . import SellbotLegFactoryCogs
from . import LawbotLegFactorySpec
from . import LawbotLegFactoryCogs


def getFactorySpecModule(factoryId):
    return FactorySpecModules[factoryId]


def getCogSpecModule(factoryId):
    return CogSpecModules[factoryId]


FactorySpecModules = {
    ToontownGlobals.SellbotFactoryInt: tt_f_ara_fac_layout00,
    ToontownGlobals.SellbotFactoryIntS: tt_f_ara_fac_layout00,
    ToontownGlobals.LawbotOfficeInt: LawbotLegFactorySpec
}

CogSpecModules = {
    ToontownGlobals.SellbotFactoryInt: tt_f_ara_fac_layout00Cogs,
    ToontownGlobals.SellbotFactoryIntS: tt_f_ara_fac_layout00Cogs,
    ToontownGlobals.LawbotOfficeInt: LawbotLegFactoryCogs
}

if __dev__:
    from . import FactoryMockupSpec
    FactorySpecModules[ToontownGlobals.MockupFactoryId] = FactoryMockupSpec
    from . import FactoryMockupCogs
    CogSpecModules[ToontownGlobals.MockupFactoryId] = FactoryMockupCogs
