from typing import List

from problems.y2025.m10.lc2_add_two_numbers import Solution, create_linked_list, linked_list_to_list


class TestFriendlySolution(Solution):
    """
    Lớp này ghi đè hàm addTwoNumbers để hỗ trợ đầu vào/đầu ra là list Python
    chỉ trong môi trường test, trong khi vẫn gọi logic cộng Linked List gốc.
    """

    def addTwoNumbers(self, l1_list: List[int], l2_list: List[int]) -> List[int]:
        # 1. Chuyển đổi đầu vào list thành Linked List (ListNode)
        l1_node = create_linked_list(l1_list)
        l2_node = create_linked_list(l2_list)

        # 2. Gọi hàm gốc (không thay đổi chữ ký hàm gốc)
        result_node = super().addTwoNumbers(l1_node, l2_node)

        # 3. Chuyển đổi kết quả ListNode về list Python để so sánh
        return linked_list_to_list(result_node)


def test_basic_list():
    assert TestFriendlySolution().addTwoNumbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]


def test_empty_list():
    assert TestFriendlySolution().addTwoNumbers([0], [0]) == [0]


def test_diff_list():
    assert TestFriendlySolution().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]
