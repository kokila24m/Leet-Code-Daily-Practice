class Solution(object):
    
    """
    Logic :
    If both strings are made by repeating the same pattern, then putting them together in any order gives the same result.
    The longest pattern that can repeat to make both strings is as long as the GCD of their lengths.
    """

    def gcd(self , a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, s1, s2):
        if s1 + s2 != s2 + s1:
            return ""
        gcd_length = self.gcd(len(s1), len(s2))
        return s1[:gcd_length]


# Time Complexity : O(n)
# Space Complexity : O(1)