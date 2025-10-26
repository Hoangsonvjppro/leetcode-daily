"""
Title: add-two-numbers
ID: 2
Tags: LinkedList,Math,Recursion
Difficulty: medium
Link: https://leetcode.com/problems/add-two-numbers/description/
Time: TBD
Space: TBD
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head


def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sum_val = val1 + val2 + carry

            carry = sum_val // 10
            digit = sum_val % 10

            new_node = ListNode(digit)
            current.next = new_node

            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy_head.next


"""
Đề: bạn được cấp 2 danh sách liên kết không rỗng biểu diển hai số nguyên không âm. Các số được lưu trữ theo thứ tự ngược
   lại và mỗi nút lưu trữ một sô nguyên duy nhất. Cộng hai dãy số và trả về kết quả dưới dạng danh sách.
   - Có thể cho rằng hai danh sách này không có số 0 đứng đầu hoặc chứa chính số 0.

   Ý tưởng:
   Tạo lần lượt hai biến num_l1 và num_l2 chứa để chứa số nguyên được lấy ra bằng cách duyệt lần lượt từ cuối danh sách lên đầu:
        Sau khi thu được hai biến num_l1 và num_l2, tôi sẽ tính tổng của chúng:
            Khí có tổng của chúng, tôi sẽ gán các số từ cuối lên đầu vào danh sách liên kết để thành một danh sách liên kết mới.
"""
