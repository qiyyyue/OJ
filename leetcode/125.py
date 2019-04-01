class Solution:
    def isPalindrome(self, s: str) -> bool:

        def proStr(org_s: str) -> str:
            res_s = ""
            for c in org_s:
                if (ord(c) >= ord('a') and ord(c) <= ord('z')) or ord(c) >= ord('0') and ord(c) <= ord('9'):
                    res_s += c
                elif (ord(c) >= ord('A') and ord(c) <= ord('Z')):
                    res_s += chr(ord(c) + 32)
            return res_s

        tmp_s = proStr(s)

        for i in range(len(tmp_s) // 2):
            if tmp_s[i] != tmp_s[len(tmp_s) - i - 1]:
                return False

        return True