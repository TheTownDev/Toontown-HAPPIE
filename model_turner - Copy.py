from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import *


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.model = loader.loadModel('ttr_m_ara_lhq_officesZone08a.bam')
        self.model.reparentTo(render)
        
        poses = [(Point3(6, 4.4, 0), 160),
        (Point3(2, 6.3, 0), 170),
        (Point3(-2, 6.3, 0), 190),
        (Point3(-6, 4.4, 0), 200)]
        
        self.foreman = []
        
        for i in range(4):
            self.room = Actor('TheFactoryForeman.bam', {'grunt': 'ttr_a_ene_cgb_neutral.bam'})
            self.room.reparentTo(render)
            self.room.setBlend(frameBlend=True)
            self.room.loop('grunt')
            self.room.setPos(poses[i][0])
            self.room.setH(poses[i][1])
            self.foreman.append(self.room)
        
        base.camLens.setFov(90)
        base.cam.place()
        base.cam.reparentTo(self.foreman[0])
        
        #base.oobe()
        
app = MyApp()
app.run()