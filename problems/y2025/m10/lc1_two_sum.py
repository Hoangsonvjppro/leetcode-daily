"""
Title: two-sum
ID: 1
Tags: array,hashmap
Difficulty: easy
Link: https://leetcode.com/problems/two-sum/description/
Time: TBD
Space: TBD
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) < 2:
            return []

        if len(nums) == 2:
            return [0, 1] if nums[0] + nums[1] == target else []

        all_negative = all(num < 0 for num in nums)
        all_positive = all(num > 0 for num in nums)
        if all_negative and target > 0:
            return []
        if all_positive and target < 0:
            return []

        for left in range(len(nums) - 1):
            for right in range(left + 1, len(nums)):
                if nums[left] + nums[right] == target:
                    return [left, right]

        return []


"""
Đề:
Cho một mảng các số nguyên nums và số nguyên target, trả về chỉ số của hai số trong mảng mà tổng của hai số đó = target
Không được sử dụng một phần tử hai lần.
Ý tưởng:
    (1)
    Cho hai vòng lặp lồng vào nhau:
        vòng lặp đầu tiên bắt đầu từ phần tử đầu tiên trong mảng -> phần tử thứ n - 1:
            vòng lặp thứ hai bắt đầu từ (phần tử đầu tiên + 1) đến phần tử thứ n:
                nếu tổng của hai phần tử trong 1 đơn vị vòng lặp tại cùng thời điểm = target:
                    -> trả về chỉ số của hai phần tử đó.
                    <-> trả về "không có hai phần tử nào trong mảng có tổng = target"
    Xử lý ngoại lệ:
    Nếu số lượng phần tử trong nums dưới 2:
        -> trả về "không có đủ hai phần tử trong mảng"
    Nếu tất cả các phẩn tử trong mảng đều là số âm trong khi target là số dương và ngược lại:
        -> trả về "tổng để tạo ra target không tồng tại"
    Nếu số lượng phần tử trong mảng = 2:
        -> trực tiếp tính tổng và trả về kết quả theo (1)
"""
