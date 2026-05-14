class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        l = n
        ans = 0

        # Edge cases
        if n == 1:
            return cost[0]
        if n == 2:
            return cost[0] + cost[1]

        # Sort descending
        cost.sort(reverse=True)

        i = 0
        x = False  # marks free candy turn

        while i < n:
            if x:  # free candy
                i += 1
                l -= 1
                x = False
                continue
            else:
                if l >= 3:
                    ans += cost[i] + cost[i + 1]
                    i += 2
                    l -= 2
                    x = True
                elif l == 1:
                    ans += cost[i]
                    break
                elif l == 2:
                    ans += cost[i] + cost[i + 1]
                    break

        return ans