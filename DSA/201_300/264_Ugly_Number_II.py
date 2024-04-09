class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 1,1,1
        product2,product3,product5 = 1,1,1
        ugly = [0] * (n+1)
        p = 1

        # stop when find the nth ugly number
        while p <= n:
            curr_min = min(product2,product3,product5)
            ugly[p] = curr_min
            p += 1

            if curr_min == product2:
                product2 = ugly[p2] * 2
                p2 += 1
            if curr_min == product3:
                product3 = ugly[p3] * 3
                p3 += 1
            if curr_min == product5:
                product5 = ugly[p5] * 5
                p5 += 1
        
        return ugly[n]