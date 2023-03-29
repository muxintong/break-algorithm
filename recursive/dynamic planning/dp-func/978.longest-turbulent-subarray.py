class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        if len(arr) == 2:
            if arr[0] == arr[1]: return 1
            else: return 2

        left = 0
        right = 0
        res = 0

        for right in range(2, len(arr), 1):
            if arr[right - 1] == arr[right]:
                left = right
            elif (arr[right - 1] - arr[right - 2]) * (arr[right] - arr[right - 1]) >= 0:
                left = right - 1
            res = max(res, right - left + 1)

        return res