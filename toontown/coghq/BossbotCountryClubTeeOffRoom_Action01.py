from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'UberZone', 'comment': '', 'parentEntId': 0, 'cogLevel': 0, 'farPlaneDistance': 1500, 'modelFilename': 'phase_12/models/bossbotHQ/ttr_m_ara_bhq_cgcZone04a', 'wantDoors': 1}, 1001: {'type': 'editMgr', 'name': 'EditMgr', 'parentEntId': 0, 'insertEntity': None, 'removeEntity': None, 'requestNewEntity': None, 'requestSave': None}, 0: {'type': 'zone', 'name': 'UberZone', 'comment': '', 'parentEntId': 0, 'scale': LVecBase3f(1, 1, 1), 'description': '', 'visibility': []}, 110102: {'type': 'moleField', 'name': '<unnamed>', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-38.6164, -26.2922, 0), 'hpr': LVector3f(0, 0, 0), 'scale': LVector3f(1, 1, 1), 'numSquaresX': 6, 'numSquaresY': 6, 'spacingX': 10.0, 'spacingY': 10.0, 'timeToPlay': 60, 'molesBase': 4, 'molesPerPlayer': 1}, 10002: {'type': 'nodepath', 'name': 'props', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 110001: {'type': 'nodepath', 'name': 'doorParent', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(60.2682, 0.55914, 0), 'hpr': LVecBase3f(270, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 19000: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(63.5969, 0.498789, 0.826069), 'hpr': LVecBase3f(-90, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_12/models/bossbotHQ/ttr_m_ara_bhq_portcullisDoor.bam'}}

GlobalEntities[19003] = {'type': 'nodepath',
          'name': 'test mover target',
          'comment': '',
          'parentEntId': 0,
          'pos': LPoint3f(0, 0, 8.98),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)}

GlobalEntities[19002] = {'type': 'mover',
          'name': 'testMover',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cycleType': 'oneWay',
          'entity2Move': 19000,
          'modelPath': 0,
          'moveTarget': 19003,
          'pos0Move': 2,
          'pos0Wait': 2,
          'pos1Move': 2,
          'pos1Wait': 2,
          'startOn': 0,
          'switchId': 110102}



Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
