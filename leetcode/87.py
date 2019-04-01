class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        c_dict = {}
        for c in s1:
            if c in c_dict:
                c_dict[c] += 1
            else:
                c_dict[c] = 1
        for c in s2:
            if c not in c_dict:
                return False
            c_dict[c] -= 1
        for c in c_dict:
            if c_dict[c] > 0:
                return False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[len(s2) - i:]) and self.isScramble(s1[i:], s2[:len(s2) - i])):
                return True
        return False