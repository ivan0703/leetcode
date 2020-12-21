class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a.reverse()
        return " ".join(a)

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords(" the sky is blue"))