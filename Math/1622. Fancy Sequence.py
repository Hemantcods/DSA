MOD=10**9+7
class Fancy:
    def __init__(self):
        self.fancy=[]
        self.add=0
        self.mul=1

    def append(self, val: int) -> None:
        val=(val-self.add)*pow(self.mul,MOD-2,MOD)
        val%=MOD
        self.fancy.append(val)
    def addAll(self, inc: int) -> None:
        self.add=(self.add+inc)%MOD
    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.fancy):
            return -1
        return (self.fancy[idx]*self.mul+self.add)%MOD          


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)