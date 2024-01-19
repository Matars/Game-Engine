
class Light:
    def __init__(self, initPos: list[float, float, float], ambInt: float, ambColor: list[float, float, float]) -> None:
        self.currentPos = initPos
        self.ambInt = ambInt
        self.ambColor = ambColor
        self.intensity = 1.0

    def getPos(self) -> list[float, float, float]:
        return self.currentPos
    
    def getAmbInt(self) -> float:
        return self.ambInt

    def getAmbCol(self) -> float:
        return self.ambColor

    def setPos(self, pos: list[float, float, float]) -> None:
        self.currentPos = pos
