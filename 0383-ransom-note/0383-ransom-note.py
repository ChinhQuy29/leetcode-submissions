class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mpp = {}
        for c in magazine:
            if c not in mpp:
                mpp[c] = 1
            else:
                mpp[c] += 1
        
        for c in ransomNote:
            if c not in mpp or mpp[c] == 0:
                return False
            mpp[c] -= 1
        
        return True