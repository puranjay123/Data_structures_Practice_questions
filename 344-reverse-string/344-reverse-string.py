class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size =len(s)
        i=0
        for i in range(size//2):
            s[i],s[-i-1] = s[-i-1],s[i]
        