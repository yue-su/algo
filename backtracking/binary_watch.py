class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return list(f"{i}:{j:02d}" for j in range(60) for i in range(12) if turnedOn == bin(i).count('1') + bin(j).count('1'))
