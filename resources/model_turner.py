from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.room = loader.loadModel('golf_outdoor_zone.bam')
        self.room.reparentTo(render)
        
        self.camera.place()
        
        camera.reparentTo(self.room)
        
        

app = MyApp()
app.run()