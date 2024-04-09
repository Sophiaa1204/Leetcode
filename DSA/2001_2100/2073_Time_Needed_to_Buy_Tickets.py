class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # 1 <= tickets[i] <= 100
        tickets[k] += 200
        cnt = 0

        while tickets:
            customer = tickets.pop(0)
            cnt += 1
            customer -= 1
            if customer == 0:
                continue
            if customer == 200:
                return cnt
            tickets.append(customer)