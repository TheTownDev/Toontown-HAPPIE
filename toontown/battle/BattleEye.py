import random
from toontown.battle.BattleBase import *
from direct.showbase.DirectObject import DirectObject
from toontown.battle import SuitBattleGlobals

class BattleEye(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleEye')

    def __init__(self, battle):
        DirectObject.__init__(self)
        self.battle = battle

    def chooseToonToTarget(self):
        toons = self.battle.activeToons[:]

        #check if there are any toons that are dead
        for toonId in toons:
            toon = self.battle.getToon(toonId)
            if toon.hp <= 0:
                toons.remove(toon)

        #if there are no toons left alive, choose a random toon
        if len(toons) == 0:
            toons = self.battle.activeToons[:]

        return self.battle.activeToons.index(random.choice(toons))

    def chooseToonActualToTarget(self):
        toons = self.battle.activeToons[:]

        #check if there are any toons that are dead
        for toonId in toons:
            toon = self.battle.getToon(toonId)
            if toon.hp <= 0:
                toons.remove(toonId)

        #if there are no toons left alive, choose a random toon
        if len(toons) == 0:
            toons = self.battle.activeToons[:]

        toonId = random.choice(toons)
        toon = self.battle.getToon(toonId)
        return toon

    def chooseSuitToTarget(self):
        active_suits = self.battle.activeSuits[:]

        #if it's dead, remove it from the list
        for suit in active_suits:
            if suit.hp <= 0:
                active_suits.remove(suit)

        #if there are no more active suits, choose a random suit
        if len(active_suits) == 0:
            active_suits = self.battle.activeSuits[:]

        return random.choice(active_suits)

    def checkGetIfCertainSuitIsInBattle(self, suitName):
        for suit in self.battle.activeSuits:
            if suit.name == suitName:
                return suit

        return None

    def addEffectToEffectHandlingAvatar(self, effectClassName, effectShortName, avatar, value=None):
        """
        tgt_suit.effectHandler.addEffect('BattleEffectExtraDamageAI')
                            dmg_eff = tgt_suit.effectHandler.children['damageBonus']
                            dmg_eff.children['value'] = 22
        """

        avatar.effectHandler.addEffect(effectClassName)
        effect = avatar.effectHandler.children[effectShortName]
        effect.startEffect()

        if value is not None:
            effect.children['value'] = value

    def getEffectFromEffectHandlingAvatar(self, effectShortName, avatar):
        return avatar.effectHandler.children[effectShortName]

    def getAttackTypeForSuit(self, suit, attack):
        attacks = SuitBattleGlobals.getSuitAttacks(suit.dna.name)
        atk = SuitBattleGlobals.pickSuitAttack(attacks, suit.getLevel())
        return atk

    def getIfSuitAttackAffectsGroup(self, suit, attack):
        attacks = SuitBattleGlobals.getSuitAttacks(suit.dna.name)
        atkInfo = SuitBattleGlobals.getSuitAttack(suit.dna.name, suit.getActualLevel(), attack)

        return atkInfo['group'] != SuitBattleGlobals.ATK_TGT_SINGLE

    def damageAllActiveToons(self, damage):
        for toonId in self.battle.activeToons:
            toon = self.battle.getToon(toonId)
            toon.hp -= damage

    def damageASingleToon(self, toonId, damage):
        toon = self.battle.getToon(toonId)
        toon.hp -= damage

    def addSuitAttackForSuit(self, suit):
        attack_movie = [NO_ID, SuitAttackType.NO_ATTACK.getId(), -1, [], 0, 0, 0]

        attack_movie[SUIT_ID_COL] = suit.doId
        attack_movie[SUIT_ATK_COL] = self.getAttackTypeForSuit(suit, attack_movie[SUIT_ATK_COL])

        atkInfo = SuitBattleGlobals.getSuitAttack(suit.dna.name, suit.getActualLevel(), attack_movie[SUIT_ATK_COL])
        atkHP = atkInfo['hp']

        if self.getIfSuitAttackAffectsGroup(suit, attack_movie[SUIT_ATK_COL]):
            attack_movie[SUIT_TGT_COL] = -1
            attack_movie[SUIT_HP_COL] = [atkHP] * len(self.battle.activeToons)
            self.damageAllActiveToons(atkHP)
        else:
            attack_movie[SUIT_TGT_COL] = self.chooseToonToTarget()
            attack_movie[SUIT_HP_COL] = [atkHP]
            self.damageASingleToon(self.battle.activeToons[attack_movie[SUIT_TGT_COL]], atkHP)

        if suit.currHP > 0:
            self.battle.suitAttacks.append(attack_movie)

    def getLeftRightSuitsAroundSuit(self, suit):
        leftSuits = []
        suitIndex = self.battle.activeSuits.index(suit)

        others = []
        if len(self.battle.activeSuits) >= 4:
            if suitIndex == 0:
                try:
                    others.append(self.battle.activeSuits[1].doId)
                except:
                    pass

            if suitIndex == 1:
                try:
                    others.append(self.battle.activeSuits[2].doId)
                except:
                    pass

            if suitIndex == 2:
                try:
                    others.append(self.battle.activeSuits[3].doId)
                except:
                    pass

                try:
                    others.append(self.battle.activeSuits[1].doId)
                except:
                    pass

            if suitIndex == 3:
                try:
                    others.append(self.battle.activeSuits[2].doId)
                except:
                    pass
        if len(self.battle.activeSuits) == 3:

            if suitIndex == 0:
                try:
                    others.append(self.battle.activeSuits[1].doId)
                except:
                    pass

            if suitIndex == 1:
                try:
                    others.append(self.battle.activeSuits[2].doId)
                except:
                    pass

                try:
                    others.append(self.battle.activeSuits[0].doId)
                except:
                    pass

            if suitIndex == 2:
                try:
                    others.append(self.battle.activeSuits[1].doId)
                except:
                    pass
        else:
            if len(self.battle.activeSuits) != 1:
                if suitIndex == 0:
                    try:
                        others.append(self.battle.activeSuits[1].doId)
                    except:
                        pass

                if suitIndex == 1:
                    try:
                        others.append(self.battle.activeSuits[0].doId)
                    except:
                        pass

        for otherSuitId in others:
            otherSuit = self.battle.findSuit(otherSuitId)
            if otherSuit.currHP <= 0:
                others.remove(otherSuitId)

        return others