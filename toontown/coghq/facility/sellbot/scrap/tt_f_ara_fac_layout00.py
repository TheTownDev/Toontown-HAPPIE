from toontown.toonbase import TTLocalizer
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'UberZone', 'comment': '', 'parentEntId': 0, 'cogLevel': 0, 'farPlaneDistance': 1500.0, 'modelFilename': 'phase_10/models/cashbotHQ/ttr_m_ara_chq_mintZone03a', 'wantDoors': 1}, 1001: {'type': 'editMgr', 'name': 'EditMgr', 'parentEntId': 0, 'insertEntity': None, 'removeEntity': None, 'requestNewEntity': None, 'requestSave': None}, 0: {'type': 'zone', 'name': 'UberZone', 'comment': '', 'parentEntId': 0, 'scale': LVecBase3f(1, 1, 1), 'description': '', 'visibility': []}, 10001: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(111.809, 548.229, 0.520435), 'hpr': LVecBase3f(90, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone04'}, 10002: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 112.07, 0), 'hpr': LVecBase3f(90, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone07'}, 10003: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-113.597, 437.982, -9.55778), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone10'}, 10004: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-349.652, 735.04, 4.97424), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone09'}, 10005: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-110.792, 102.449, 9.69004), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone21'}, 10006: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-205.99, 327.795, 5.45199), 'hpr': LVecBase3f(90, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone04'}, 10007: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-473.125, 213.803, 9.69), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone07'}, 10008: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-350.523, 500.569, 4.7405), 'hpr': LVecBase3f(90, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone13a'}, 10009: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-650.277, 687.677, 5.11115), 'hpr': LVecBase3f(90, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone09'}, 100010: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-251.526, 658.316, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone21'}, 100011: {'type': 'model', 'name': 'room', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-720.354, 915.495, 5.03059), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_factoryZone21'}, 18200: {'type': 'model', 'name': '<unnamed>', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(8, 8, 8), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_extSkybox.bam'}, 24200: {'type': 'battleBlocker', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(-48.4095, 0, 0), 'hpr': LVecBase3f(270, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'cellId': 0, 'radius': 10.0}, 24201: {'type': 'battleBlocker', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(22.4673, 0, 0), 'hpr': LVecBase3f(270, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'cellId': 1, 'radius': 10.0}, 24202: {'type': 'battleBlocker', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(-16.2008, 41.8264, 9.83413), 'hpr': LVecBase3f(90, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'cellId': 2, 'radius': 22.0}, 30000: {'type': 'path', 'name': 'copy of <unnamed>', 'comment': '', 'parentEntId': 10004, 'pos': LPoint3f(1, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'pathIndex': 5, 'pathScale': 1.0}, 30010: {'type': 'goon', 'name': '<unnamed>', 'comment': '', 'parentEntId': 30000, 'pos': LPoint3f(0, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': 1.5, 'attackRadius': 15, 'crushCellId': None, 'goonType': 'pg', 'gridId': None, 'hFov': 70, 'strength': 7, 'velocity': 6.0}, 30030: {'type': 'path', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10004, 'pos': LPoint3f(0, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'pathIndex': 41, 'pathScale': 1.0}, 30060: {'type': 'goon', 'name': '<unnamed>', 'comment': '', 'parentEntId': 30000, 'pos': LPoint3f(0, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': 1.5, 'attackRadius': 15, 'crushCellId': None, 'goonType': 'pg', 'gridId': None, 'hFov': 70, 'strength': 7, 'velocity': 4}}


for i in range(1):
     GlobalEntities[30000 + i] = {'type': 'path',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10004,
         'pos': Point3(1, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'pathIndex': 5,
         'pathScale': 1.0}

for i in range(1):
     GlobalEntities[30010 + i] = {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 30000,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1.5,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': 7,
         'velocity': 6.0}

"""


for i in range(1):
     GlobalEntities[30030 + i] = {'type': 'path',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10004,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'pathIndex': 41,
         'pathScale': 1.0}

for i in range(1):
     GlobalEntities[30060 + i] = {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 30000,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1.5,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': 7,
         'velocity': 4}

for i in range(1):
     GlobalEntities[30060 + i] = {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 30000,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1.5,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': 7,
         'velocity': 4}




for i in range(1):
     GlobalEntities[18250 + i] = {'type': 'model',
              'name': '<unnamed>',
              'comment': '',
              'parentEntId': 0,
              'pos': Point3(0, 0, 0),
              'hpr': Vec3(0, 0, 0),
              'scale': Vec3(1, 1, 1),
              'collisionsOnly': 0,
              'flattenType': 'light',
              'loadType': 'loadModelCopy',
              'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_sellbotLegFactory.bam'}


for i in range(1):
     GlobalEntities[18200 + i] = {'type': 'model',
              'name': '<unnamed>',
              'comment': '',
              'parentEntId': 0,
              'pos': Point3(0, 0, 0),
              'hpr': Vec3(0, 0, 0),
              'scale': Vec3(1, 1, 1),
              'collisionsOnly': 0,
              'flattenType': 'light',
              'loadType': 'loadModelCopy',
              'modelPath': 'phase_9/models/cogHQ/ttr_m_ara_shq_extSkybox.bam'}
"""

Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
