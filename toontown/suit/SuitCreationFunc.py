from toontown.suit import Suit, SuitDNA

def createClientSuit(self, dnaName):
    demotedCeo = Suit.Suit()
    demotedCeo.dna = SuitDNA.SuitDNA()
    demotedCeo.dna.newSuit(dnaName)
    demotedCeo.setDNA(demotedCeo.dna)
    demotedCeo.reparentTo(render)
    demotedCeo.loop('neutral')
    
    return demotedCeo