class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.moved = False
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.perimeter
        self.moved = True

    def getPos(self) -> List[int]:
        p = self.pos
        if p < self.w:
            return [p, 0]
        p -= self.w - 1
        if p < self.h:
            return [self.w - 1, p]
        p -= self.h - 1
        if p < self.w:
            return [self.w - 1 - p, self.h - 1]
        p -= self.w - 1
        return [0, self.h - 1 - p]

    def getDir(self) -> str:
        p = self.pos
        if p == 0:
            return "South" if self.moved else "East"
        elif p <= self.w - 1:
            return "East"
        elif p <= self.w + self.h - 2:
            return "North"
        elif p <= 2 * self.w + self.h - 3:
            return "West"
        else:
            return "South"