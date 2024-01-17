
class Light:
    def __init__(self, initPos: list[float, float, float]):
        self.currentPos = [0.0, 0.0, 0.0]
    
    def getPos(self) -> list[float, float, float]:
        return self.currentPos
    
    def setPos(self, pos: list[float, float, float]) -> None:
        self.currentPos = pos