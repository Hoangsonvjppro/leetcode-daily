from problems.y2025.m10.lc3_longest_substring_without_repeating_characters import Solution


def test_1():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test_2():
    assert Solution().lengthOfLongestSubstring("bbbbbbbb") == 1


def test_3():
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
