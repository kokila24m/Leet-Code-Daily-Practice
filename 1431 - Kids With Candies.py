class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        """

        Find the current maximum number of candies any kid has.
        Then check for each kid if giving them all the extra candies makes their total equal to or more than that maximum.

        """
        
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
        