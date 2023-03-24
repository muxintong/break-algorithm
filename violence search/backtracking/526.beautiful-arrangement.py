class Solution:
    def countArrangement(self, n: int) -> int:
        perms = []
        track = []

        used = [False for i in range(n + 1)]

        def backtrack(used: List[bool]) -> None:
            if len(track) == n:
                perms.append(track.copy())

            for i in range(1, n + 1):
                if used[i]: continue
                used[i] = True
                track.append(i)

                backtrack(used)

                track.remove(i)
                used[i] = False

        backtrack(used)

        res = []
        for perm in perms:
            flag = 0
            for i in range(1, len(perm) + 1):
                if perm[i - 1] % i != 0 and i % perm[i - 1] != 0:
                    flag = 1
                    break
            if flag == 0: res.append(perm)

        return len(res)