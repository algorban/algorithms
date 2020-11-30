from collections import deque

class Solution:

    def can_break(self, s, wordDict):
        N = len(string)
        dp = [False for _ in range(N+1)]
        dp[0] = True

        for end in range(1, N+1):
            for start in range(end-1, -1, -1):
                if s[start:end] in wordDict and dp[start]:
                    dp[end] = True
        return dp[N]


    def combinations(self, s, wordDict):
        result = []
        q = deque([(s, [])])
        while q:
            string, path = q.popleft()
            if not string:
                result.append(path)
            for i in range(len(string)+1):
                if string[:i] in wordDict:
                    q.append((string[i:], path + [string[:i]]))
        return result


if __name__ == '__main__':
    s = Solution()
    string = "facebook"
    wordDict = {"face", "bouk", "boo", "book", "facebook", "bo", "ok"}
    print(s.can_break(string, wordDict))
    print(s.combinations(string, wordDict))