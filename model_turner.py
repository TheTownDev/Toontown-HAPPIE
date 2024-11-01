from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.room = loader.loadModel('phase_12/models/bossbotHQ/ttr_m_ara_bhq_cgcZone18a.bam')
        self.room.reparentTo(render)
        self.room.setH(180)
        
        self.accept('p', self.writeNewBamModel)
    
    def writeNewBamModel(self):
        self.folderPath = 'phase_12/models/bossbotHQ/'
        self.room.writeBamFile(self.folderPath + 'ttr_m_ara_bhq_cgcZone18b.bam')

app = MyApp()
app.run()