class Solution:
    """
    Given an array arr[] of N integers, the task is to sort the array in non-decreasing order by performing the minimum
    number of operations. In a single operation, an element of the array can either be incremented or decremented by 1.
    Print the minimum number of operations required.
    """
    def getMinimumOps(self, ar):

        # Number of elements in the array
        n = len(ar)
        # Smallest element in the array
        small = min(ar)
        # Largest element in the array
        large = max(ar)
        """ 
            dp(i, j) represents the minimum number 
            of operations needed to make the 
            array[0 .. i] sorted in non-decreasing 
            order given that ith element is j 
        """
        dp = [[0 for i in range(large + 1)]
              for i in range(n)]

        # Fill the dp[]][ array for base cases
        for j in range(small, large + 1):
            dp[0][j] = abs(ar[0] - j)
        """ 
        /* 
            Using results for the first (i - 1) 
            elements, calculate the result 
            for the ith element 
        */ 
        """
        for i in range(1, n):
            minimum = 10 ** 9
            for j in range(small, large + 1):
                # """
                #     /*
                #     If the ith element is j then we can have
                #     any value from small to j for the i-1 th
                #     element
                #     We choose the one that requires the
                #     minimum operations
                # """
                minimum = min(minimum, dp[i - 1][j])
                dp[i][j] = minimum + abs(ar[i] - j)
        """ 
        /* 
            If we made the (n - 1)th element equal to j 
            we required dp(n-1, j) operations 
            We choose the minimum among all possible 
            dp(n-1, j) where j goes from small to large 
        */ 
        """
        ans = 10 ** 9
        for j in range(small, large + 1):
            ans = min(ans, dp[n - 1][j])

        return ans


if __name__ == '__main__':
    array = [1, 2, 1, 4, 3]
    s = Solution()
    print(s.getMinimumOps(array))