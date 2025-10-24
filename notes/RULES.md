# notes/RULES.md
# RULES: Chuẩn code cho LeetCode (Python)

> Mục tiêu: code **đọc hiểu nhanh**, **đúng độ phức tạp**, **dễ test**, **tránh lạm dụng** thư viện/built-ins.

---

## 0) Nguyên tắc chung (bắt buộc)
1. **Không I/O** trong solution: không `input()`, không `print()`; chỉ lớp `Solution` + method.
2. **Type hints** đầy đủ (Py 3.13): dùng `list[int]`, `dict[str, int]`, `set[int]`…
3. **Header bắt buộc** ở đầu file (metadata + Time/Space + 1–2 câu “Approach”).
4. **Tên biến có nghĩa** (`left/right`, `freq`, `stack`, `res`); tránh `l`, `r`, `tmp` tràn lan.
5. **Không side-effects** toàn cục: không biến global, không sửa input nếu không cần.
6. **Độ phức tạp** đúng mục tiêu: không đẩy từ O(n) lên O(n log n) để “dễ viết”.
7. **Test bắt buộc**: tối thiểu 2 case (có case biên).
8. Code **pass**: `ruff check .`, `black .`, `pytest -q`. Nếu fail → không commit lên `main`.

---

## 1) Độ phức tạp & tiêu chí theo độ khó
| Độ khó | Thời gian khuyến nghị | Ghi chú |
|---|---|---|
| Easy | O(n) hoặc O(n log n) (nếu cần sort) | Tránh O(n^2) nếu có cách tốt hơn |
| Medium | O(n)–O(n log n) | O(n^2) chỉ khi ràng buộc nhỏ hoặc bài bản chất yêu cầu |
| Hard | O(n log n), O(n^2) có chọn lọc | Luôn ghi trade-off & vì sao chấp nhận |

Bộ nhớ: **O(1)–O(n)** tùy bài; giải thích nếu dùng cấu trúc tốn thêm.

---

## 2) Chuẩn thư viện & built-ins (được phép / hạn chế / cấm)

### 2.1 **Được phép** (khuyến khích đúng chỗ)
| Mục | Cho phép | Dùng khi | Ghi chú |
|---|---|---|---|
| Sort | `sorted()`, `list.sort()` | Hai con trỏ/merge intervals/greedy cần sort | Không dùng để “né” giải O(n) |
| Tập hợp | `set`, `dict` | Tra cứu O(1), visited, two-sum | Dùng `.get`, `.setdefault` gọn |
| Đếm | `collections.Counter` | Đếm tần suất | Tránh `most_common()` cho Top-K lớn |
| Hàng đợi/ngăn xếp | `collections.deque` | BFS/queue/stack | `append`, `appendleft`, `popleft` |
| Heap | `heapq` | Top-K, K-way merge, Dijkstra | Ưu tiên heap thay vì sort toàn bộ |
| Tìm kiếm nhị phân | `bisect_left/right` | Mảng **đã sort**, LIS (patience) | Rõ ý hơn tự viết |
| Toán | `math` | `gcd`, `sqrt`, `inf` | Tránh trick khó đọc |
| DP memo | `functools.lru_cache` | Top-down DP | Thêm `maxsize=None` nếu cần |
| Tổ hợp cơ bản | `itertools.accumulate`, `pairwise` | Prefix sum, quét cạnh | Tránh comp lồng phức |

### 2.2 **Hạn chế** (chỉ dùng nếu làm **rõ ràng hơn**)
| Mục | Ví dụ | Lý do |
|---|---|---|
| Comprehension nhiều tầng | List/dict comp lồng >2 | Khó đọc, khó debug |
| `Counter.most_common()` | Top-K trên n lớn | O(n log n); heap tốt hơn |
| Đệ quy sâu | DFS đồ thị lớn | Dễ stack overflow; ưu tiên `deque`/stack tay |
| `itertools.permutations/combinations` | Brute force | Chỉ dùng khi n nhỏ, ghi rõ |

### 2.3 **Cấm** (trong solution)
- Lib ngoài chuẩn: **pandas, numpy, networkx, scipy…**
- I/O console/file, sleep, random (trừ khi bài yêu cầu).
- Reflection/magics/`exec`/`eval`.
- Golf code, one-liner bí hiểm, micro-optimization rối mắt.

---

## 3) API/hàm được dùng (chi tiết)

### List
- ✅ `append`, `pop`, `extend`, `reverse`, `sort`, slicing có kiểm soát  
- ⚠️ Tránh `insert(0, x)`, `pop(0)` (O(n)) → dùng `deque`

### Dict / Set
- ✅ `get`, `setdefault`, membership `in`  
- ⚠️ Không mutate dict khi đang iterate keys (cần thì copy key trước)

### String
- ✅ `''.join(parts)` để build  
- ⚠️ Tránh `s += piece` trong vòng lặp lớn

### Heap
- ✅ `heapq.heappush`, `heapq.heappop`, `heapq.heapreplace`, `heapq.nsmallest`  
- Max-heap: dùng `(-key, val)` hoặc wrapper

### Bisect
- ✅ `bisect_left(a, x)`, `bisect_right(a, x)` trên mảng **đã sort**

### Collections
- ✅ `deque([...])`, `popleft()`, `appendleft()`  
- ✅ `Counter` (đếm), `defaultdict(list/int/set)`

---

## 4) Template file solution (bắt buộc)
```python
"""
Title: <tên bài>
ID: <id hoặc N/A> | Tags: <a,b,c> | Difficulty: <easy|medium|hard>
Link: <url>
Time: O(...)
Space: O(...)
Approach: <1–2 câu tóm tắt ý tưởng + vì sao đúng/độ phức tạp>
"""

class Solution:
    def solve(self, ...):
        # 1) Khởi tạo cấu trúc dữ liệu
        # 2) Thuật toán chính (rõ ràng, không one-liner bí hiểm)
        # 3) Trả kết quả
        ...
