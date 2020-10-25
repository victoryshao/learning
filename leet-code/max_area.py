class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            max_area = max(min(height[left], height[right]) * (right - left), max_area)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    s = Solution()
    while True:
        raw = input("Input:")
        if raw == "end":
            break

        try:
            num = list(map(int, raw.rstrip(",").split(",")))
            print(s.maxArea(num))
        except ValueError:
            break
