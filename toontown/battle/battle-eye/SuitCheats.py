import typing
from dataclasses import dataclass
from typing import Set, List, Union
from toontown.battle.SuitBattleGlobals import *
from toontown.suit.SuitDNA import *
import random


@dataclass
class SuitCheat:
    key:   str  # The key that the codebase references for the cheat.
    movieIndex : int # The index of the movie to play.
    targeting : int # The index of the targeting type [0 is single, 1 is all].

    def unique_key(self) -> str:
        return f"{self.key}-{self.suit}"

    def __hash__(self):
        return self.unique_key().__hash__()