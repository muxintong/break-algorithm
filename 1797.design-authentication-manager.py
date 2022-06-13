class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenId = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenId.setdefault(tokenId, currentTime)

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokenId.get(tokenId) and currentTime < self.timeToLive + self.tokenId.get(tokenId):
            self.tokenId[tokenId] = currentTime
        else:
            return

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        times = self.tokenId.values()
        for time in times:
            if time + self.timeToLive > currentTime:
                res += 1
        return res


# 构造 AuthenticationManager ，设置 timeToLive = 5 秒。
authenticationManager = AuthenticationManager(5)
# 时刻 1 时，没有验证码的 tokenId 为 "aaa" ，没有验证码被更新。
print(authenticationManager.renew("aaa", 1))
# 时刻 2 时，生成一个 tokenId 为 "aaa" 的新验证码。
print(authenticationManager.generate("aaa", 2))
# 时刻 6 时，只有 tokenId 为 "aaa" 的验证码未过期，所以返回 1 。
print(authenticationManager.countUnexpiredTokens(6))
# 时刻 7 时，生成一个 tokenId 为 "bbb" 的新验证码。
print(authenticationManager.generate("bbb", 7))
# tokenId 为 "aaa" 的验证码在时刻 7 过期，且 8 >= 7 ，所以时刻 8 的renew 操作被忽略，没有验证码被更新。
print(authenticationManager.renew("aaa", 8))
# tokenId 为 "bbb" 的验证码在时刻 10 没有过期，所以 renew 操作会执行，该 token 将在时刻 15 过期。
print(authenticationManager.renew("bbb", 10))
# tokenId 为 "bbb" 的验证码在时刻 15 过期，tokenId 为 "aaa" 的验证码在时刻 7 过期，所有验证码均已过期，所以返回 0 。
print(authenticationManager.countUnexpiredTokens(15))
