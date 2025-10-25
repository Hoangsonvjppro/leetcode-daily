from problems.y2025.m10.lc1_two_sum import Solution


def test_basic_pair():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_no_pair():
    assert Solution().twoSum([1, 2, 3], 7) == []


def test_negative_target_unreachable():
    assert Solution().twoSum([5, 6, 7], -1) == []


def test_pair_late_in_array():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_empty_list():
    assert Solution().twoSum([], 6) == []


def test_array_has_only_two_number():
    assert Solution().twoSum([4, 5], 9) == [0, 1]
