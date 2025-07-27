import os
from abc import ABC, abstractmethod
from typing import Self

class PointsAwardable(ABC):
    def __init__(self, pointsAwarded) -> None:
        self.pointsAwarded = pointsAwarded

    def getPointsAwarded(self) -> int:
        return self.pointsAwarded

class GameAction(PointsAwardable):
    def __init__(self, pointsForAction) -> None:
        super().__init__(pointsForAction)
    
    @abstractmethod
    def __lt__(self, gameAction: Self):
        pass

    @abstractmethod
    def __eq__(self, gameAction: Self):
        pass
        

class PlayRock(GameAction):
    def __init__(self):
        super().__init__(1)
    
    def __lt__(self, gameAction) -> bool:
        if isinstance(gameAction, PlayPaper):
            return True
        return False

    def __eq__(self, gameAction):
        if isinstance(gameAction, PlayRock):
            return True
        return False

class PlayPaper(GameAction):
    def __init__(self):
        super().__init__(2)

    def __lt__(self, gameAction) -> bool:
        if isinstance(gameAction, PlayScissors):
            return True
        return False

    def __eq__(self, gameAction):
        if isinstance(gameAction, PlayPaper):
            return True
        return False

class PlayScissors(GameAction):
    def __init__(self):
        super().__init__(3)

    def __lt__(self, gameAction) -> bool:
        if isinstance(gameAction, PlayRock):
            return True
        return False

    def __eq__(self, gameAction):
        if isinstance(gameAction, PlayScissors):
            return True
        return False

class GameResult(PointsAwardable):
    def __init__(self, pointsForResult):
        super().__init__(pointsForResult)

class LoseAction(GameResult):
    def __init__(self):
        super().__init__(0)

class DrawAction(GameResult):
    def __init__(self):
        super().__init__(3)

class WinAction(GameResult):
    def __init__(self):
        super().__init__(6)

class GameRound():
    def __init__(self, playerAAction, playerBAction):
        self.playerAAction = playerAAction
        self.playerBAction = playerBAction
    
    def getResult(self) -> GameResult:
        if self.playerAAction < self.playerBAction:
            return WinAction()
        elif self.playerAAction == self.playerBAction:
            return DrawAction()
        else:
            return LoseAction()

class GameActionFactory():
    def __init__(self) -> None:
        pass

    def createPlayerAGameAction(self, symbol: str) -> GameAction:
        if symbol == "A":
            return PlayRock()
        if symbol == "B":
            return PlayPaper()
        if symbol == "C":
            return PlayScissors()
    
    def createPlayerBGameAction(self, symbol: str) ->  GameAction:
        if symbol == "X":
            return PlayRock()
        if symbol == "Y":
            return PlayPaper()
        if symbol == "Z":
            return PlayScissors()
        
        return PlayRock()

    def createPlayerBGameActionFromPlayerAAction(self, playerAAction: GameAction, playerBResult: GameResult) -> GameAction:
        possibleActions = [PlayRock(), PlayPaper(), PlayScissors()]
        if isinstance(playerBResult, LoseAction):
            for playAction in possibleActions:
                if playAction < playerAAction:
                    return playAction
        elif isinstance(playerBResult, DrawAction):
            for playAction in possibleActions:
                if playAction == playerAAction:
                    return playAction
        else:
            for playAction in possibleActions:
                if not playAction < playerAAction and not playAction == playerAAction:
                    return playAction


class GameResultFactory():
    def __init__(self) -> None:
        pass
    
    def createPlayerBGameResult(self, symbol: str) -> GameResult:
        if symbol == "X":
            return LoseAction()
        if symbol == "Y":
            return DrawAction()
        if symbol == "Z":
            return WinAction()

        return LoseAction()


answer = 0
gameActionFactory = GameActionFactory()
gameResultFactory = GameResultFactory()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as gameFile:
    for gameLine in gameFile:
        playerASymbol, playerBSymbol = gameLine.strip().split()
        playerAGameAction = gameActionFactory.createPlayerAGameAction(playerASymbol)
        playerBGameResult = gameResultFactory.createPlayerBGameResult(playerBSymbol)
        playerBGameAction = gameActionFactory.createPlayerBGameActionFromPlayerAAction(playerAGameAction, playerBGameResult)
        answer += playerBGameAction.getPointsAwarded()
        answer += playerBGameResult.getPointsAwarded()

print(f"Day 2 Puzzle 1: {answer}")