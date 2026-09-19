class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        window = {}

        have = 0
        need = len(countT)

        left = 0

        result = ""
        resultLength = float("inf")

        for right in range(len(s)):

            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:

                windowLength = right - left + 1

                if windowLength < resultLength:
                    result = s[left:right + 1]
                    resultLength = windowLength

                leftChar = s[left]

                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1

                left += 1

        return result