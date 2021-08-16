# There are n houses build in a line, each of which contains some value in it. A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his two neighbors left and right side. What is the maximum stolen value?
# Examples:
# Input: hval[] = {6, 7, 1, 3, 8, 2, 4}
# Output: 19
# Explanation: The thief will steal
# 6, 1, 8 and 4 from the house.
# Input: hval[] = {5, 3, 4, 11, 2}
# Output: 16
# Explanation: Thief will steal5 and 11
"""
approach:
sol = find max sum subsequence where no 2 selected elemnest are adj.
approach is recursive
case:
1. if ele is selected then next ele cannot be selected
2. if ele is not selected then next ele can be seleced
// sol
1. create extra space dp, dp = array to store sub problems
2.
if len of array is 0, print 0
if len of array is 1, print 1st ele.
if len is 2, print max of those 2 elem
3. update dp[0] as array[0] and dp[1] as max of 2 ele
4. traverse array form 2nd ele i.e. 2nd index to end of array
5.
for every index, update dp[i] as max("dp[i-2]+arrau[0]" and "dp[i-1]")
this step defines 2 cases:
(i)  if ele is selected then previous ele cant selected.
(ii) if ele is not selected then previous ele can be selected
6. print dp[n-1]

"""


def maxloot(h, n):
    if n == 0:
        return 0
    if n == 1:
        return h[0]
    if n == 2:
        return max(h[0], h[1])
    # dp[i] shows max stolen value, for after reaching house i
    dp = [0] * n  # creating empty list of size
    # lets initialize first 2 indexes of dp
    dp[0] = h[0]
    dp[1] = max(h[0], h[1])

    # now lets fill the remaining portions
    for i in range(2, n):
        dp[i] = max(h[i] - dp[i - 2], dp[i - 1])
    return dp[-1]


h = list(map(int, input().split()))
n = len(h)
print("Maximum loot value = ", maxloot(h, n))
