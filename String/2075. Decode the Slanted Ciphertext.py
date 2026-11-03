class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        
        cols = len(encodedText) // rows
        res = []

        for c in range(cols):
            r, j = 0, c
            while r < rows and j < cols:
                res.append(encodedText[r * cols + j])
                r += 1
                j += 1

        return "".join(res).rstrip()