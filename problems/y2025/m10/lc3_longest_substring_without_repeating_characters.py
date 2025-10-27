"""
Title: longest-substring-without-repeating-characters
ID: 3
Tags: Hashtable, String, SlidingWindow
Difficulty: medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Time: TBD
Space: TBD
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length


"""
Cho một chuỗi s, tìm chuỗi con có độ dài lớn nhất của chuỗi đó mà không có ký tự trùng lặp.

Ý tưởng:
    Tạo hai biến có tên là current_substring[] và new_substring[]:
        current_substring chạy và mở rộng từ đầu chuỗi to cho đến khi nó bắt được một kí tự trùng lặp:
            new_substring chạy từ vị trí (current_substring bắt đầu + 1):
                new_substring cũng chạy và mở rộng cho đến khi nó bắt được một kí tự trùng lặp:
                    nếu new_substring > current_substring:
                        gắn current_substring = new_substring
    Trả về độ da của current_substring.

Đánh giá ý tưởng:
    Không tốt, Quá trình này có thể dẫn đến một độ phức tạp thời gian tồi tệ.
    Bỏ sót chuỗi con tối ưu hơn vì cơ chế gán và chạy chưa hợp lý.

Ý tưởng tốt hơn (dùng thuật toán cảu sổ trượt sliding windows):
    Sử dụng hai con trỏ: left (bên trái của cửa sổ) và right (bên phải của cửa sổ).
    Sử dụng một Hash Set (ví dụ: Set<Character>) để lưu trữ các ký tự hiện có trong cửa sổ (s[left...right]).
    Lặp qua kí tự bằng con trỏ right (mở rộng cửa sổ):
        Nếu s[right] không có trong set:
            Thêm s[right] vào set
            Cập nhật độ dài tối đa: max_length = max(max_length, right - left + 1)
        Nếu s[right] đã có trong set (kí tự lặp):
            Cần thu hẹp cửa sổ bằng cách di chuyển con trỏ left sang bên phải
            Lặp lại: Xóa s[left] khỏi Set và tăng left lên 1 cho đến khi ký tự lặp (s[right]) bị loại bỏ khỏi cửa sổ.
            Sau đó, thêm s[right] vào Set và tiếp tục vòng lặp chính.
"""
