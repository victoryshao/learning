class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        num = x
        cur = 0

        while num != 0:
            cur = cur * 10 + num % 10
            num //= 10

        return cur == x


if __name__ == '__main__':
    s = Solution()
    while True:
        raw = input("Input:")
        if raw == "end":
            break

        try:
            num = int(raw)
            print(s.isPalindrome(num))
        except ValueError:
            break
