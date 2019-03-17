class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo = weights[0]
        hi = 0
        for w in weights:
            lo = max(lo, w)
            hi += w

        while lo < hi:
            mid = (lo + hi) // 2

            days = 1
            s = 0
            shipped = True

            for w in weights:

                if s + w > mid:
                    s = 0
                    days += 1
                    if days > D:
                        shipped = False
                        break
                s += w

            if shipped:
                hi = mid

            else:
                lo = mid + 1
