class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        print(j, s[j])
        clean = re.sub(r'[^a-z0-9]', '', s.lower())
        print(clean)
        return clean == clean[::-1]
        