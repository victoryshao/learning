class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        substring_map = {}
        for i in range(len(s)):
            substring = ""
            for char in s[i:]:
                if char not in substring:
                    substring += char
                    continue
                break

            substring_map[substring] = len(substring)

        return max(substring_map.values())

    def length_of_longest_substring(self, s: str):
        if not s:
            return 0

        max_len = 0
        current_len = 0
        left = 0
        windows = set()

        for i in range(len(s)):
            while s[i] in windows:
                windows.remove(s[left])
                left += 1
                current_len -= 1

            windows.add(s[i])
            current_len += 1
            max_len = max_len if current_len < max_len else current_len

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"), s.length_of_longest_substring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"), s.length_of_longest_substring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"), s.length_of_longest_substring("pwwkew"))
    print(s.lengthOfLongestSubstring(""), s.length_of_longest_substring(""))
    # print(s.length_of_longest_substring("pwwkew"))
