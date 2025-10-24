# LeetCode Daily – Python

[![CI](https://github.com/{YOUR_GH_USERNAME}/{REPO_NAME}/actions/workflows/python-ci.yml/badge.svg)](https://github.com/{YOUR_GH_USERNAME}/{REPO_NAME}/actions)

> **Mục tiêu:** Luyện thuật toán mỗi ngày theo chuẩn “backend chuyên nghiệp”: có test, có CI, repo sạch, dễ rà soát và tối ưu định kỳ.

## Cấu trúc thư mục
~~~
problems/YYYY/MM/slug.py    # Lời giải từng bài (theo ngày/tháng/năm)
tests/test_slug.py          # Unit test cho mỗi bài
notes/                      # Ghi chú patterns/ý tưởng
scripts/                    # Script tạo bài mới + chọn bài để tối ưu
.github/workflows/          # CI: lint + format + test
index.json                  # Nhật ký tiến độ + metadata
~~~

## Tiêu chuẩn chất lượng (mỗi bài)
- Header metadata: **Title/ID/Tags/Difficulty/Link/Time/Space**.
- Có **ít nhất 1–2 test** với case biên (`pytest`).
- Pass **ruff** (lint) và **black** (format).
- Tên file: `lc<ID>_<slug>.py` (vd: `lc1_two_sum.py`).
- Commit message gọn: `feat(lc<ID>): <slug> [tags]`.

## Bắt đầu nhanh
~~~
# 1) Tạo venv (Python 3.13)
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1

# 2) Cài phụ thuộc
pip install -r requirements.txt

# 3) Kiểm tra nhanh
ruff check .
black .
pytest -q
~~~

## Sinh bài mới (tự động)
~~~
python scripts/new.py "two-sum" \
  --id 1 \
  --tags "array,hashmap" \
  --difficulty easy \
  --link https://leetcode.com/problems/two-sum/
~~~
> Script sẽ tạo file lời giải theo `problems/YYYY/MM/` + test mẫu trong `tests/` và cập nhật `index.json`.

## Lịch luyện & tối ưu (policy)
- **Hằng ngày (T2–CN):** 1 bài mới.
- **Tối Thứ Tư & Tối Thứ Bảy:** *không làm bài mới*, **tối ưu 2 bài cũ** (điều kiện ≥ 7 ngày).
  ~~~
  python scripts/optimize.py --count 2 --min-days 7 --status done
  # Làm theo OPTIMIZE_TODAY.md rồi mở PR/commit
  ~~~
- **Ngày 1 các tháng chẵn (02/04/06/08/10/12):** tối ưu lần 2 **10 bài** (chọn từ các bài đã tối ưu lần 1).
- **Ngày 31/12:** thử thách 24h, tối ưu lần 3 **≥24 bài** (ưu tiên bài quan trọng/nhiều view).

### Checklist khi tối ưu (per PR)
- [ ] Bổ sung test (biên/stress) và giải thích ý tưởng 3–5 dòng.
- [ ] Dọn tên biến, tách hàm, viết docstring.
- [ ] Xác nhận **Time/Space**.
- [ ] (Tuỳ chọn) đo `timeit`/benchmark và ghi “trước/sau”.

## Featured Solutions (bắt đầu từ đây)
> Liệt kê 5–8 bài “mẫu mực” để HR/Reviewer xem trước:
- [ ] (điền link: `problems/YYYY/MM/lc<ID>_<slug>.py`) – vì sao đáng xem (1 câu).
- [ ] …
- [ ] …

## Tiến độ
- **Bắt đầu:** _(điền ngày bắt đầu)_  
- **Tổng số bài:** sinh từ `index.json` (cập nhật tự động bởi script).

## CI & Test (tóm tắt)
- **Test:** `pytest -q` – chạy tất cả bài, đảm bảo tối ưu không phá logic cũ.
- **Lint/Format:** `ruff`, `black` – giữ code sạch và thống nhất.
- **CI (GitHub Actions):** tự động lint + format-check + test mỗi lần push/PR.  
  > Sửa `{YOUR_GH_USERNAME}` và `{REPO_NAME}` trong badge ở đầu file sau khi push repo.

---

**Gợi ý:** Thêm mục “How to run locally” cho các bài cần input lớn, và cập nhật “Featured Solutions” mỗi quý để repo luôn nổi bật.
