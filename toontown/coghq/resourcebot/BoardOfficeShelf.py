from toontown.toonbase.ToontownGlobals import *
from toontown.coghq.resourcebot import BoardOfficeProduct

class BoardOfficeShelf(BoardOfficeProduct.BoardOfficeProduct):
    Models = {ResourcebotGeneralField: 'phase_10/models/cashbotHQ/shelf_A1MoneyBags',
     ResourcebotSpecialistField: 'phase_10/models/cashbotHQ/shelf_A1Money',
     ResourcebotSpecialistField2: 'phase_10/models/cashbotHQ/shelf_A1Gold'}
    Scales = {ResourcebotGeneralField: 1.0,
     ResourcebotSpecialistField: 1.0,
     ResourcebotSpecialistField2: 1.0}
