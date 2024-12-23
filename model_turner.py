from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.room = loader.loadModel('phase_4/models/props/ttr_m_ara_ext_bench.bam')
        self.room.reparentTo(render)
        
        self.room.place()
        
        camera.reparentTo(self.room)
        
        

app = MyApp()
app.run()