class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        curr_row = 0
        change = 0
        steps = [-1, 1]
        rows = [""] * (min(len(s), numRows))
        for char in s:
            rows[curr_row] += char
            if curr_row == 0 or curr_row == numRows-1:
                change += 1

            curr_row += steps[change % 2]

        return "".join(rows)