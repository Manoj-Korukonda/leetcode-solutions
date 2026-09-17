class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = []
        for i in s.rstrip()[::-1]:
            if i == ' ' :
                break
            k.append(i)
        return len(k)

            
        