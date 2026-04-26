class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        Rct=moves.count("R")
        Lct=moves.count("L")
        mvct=moves.count("_")
        res=abs(Lct-Rct)+mvct
        return res