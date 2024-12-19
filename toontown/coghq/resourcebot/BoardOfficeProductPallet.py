from toontown.toonbase.ToontownGlobals import *
from toontown.coghq.resourcebot import BoardOfficeProduct

class BoardOfficeProductPallet(BoardOfficeProduct.BoardOfficeProduct):
    Models = {ResourcebotGeneralField: 'phase_10/models/cashbotHQ/DoubleCoinStack.bam',
     ResourcebotSpecialistField: 'phase_10/models/cogHQ/DoubleMoneyStack.bam',
     ResourcebotSpecialistField2: 'phase_10/models/cashbotHQ/DoubleGoldStack.bam'}
    Scales = {ResourcebotGeneralField: 1.0,
     ResourcebotSpecialistField: 1.0,
     ResourcebotSpecialistField2: 1.0}
