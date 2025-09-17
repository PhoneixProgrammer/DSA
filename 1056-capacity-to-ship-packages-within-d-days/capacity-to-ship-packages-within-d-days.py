class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            day_count = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > capacity:
                    day_count += 1
                    current_weight = 0
                current_weight += w
            return day_count <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid  # try smaller capacity
            else:
                left = mid + 1  # need bigger capacity
        return left