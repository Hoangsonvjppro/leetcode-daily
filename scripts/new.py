# --- imports gọn để ruff không kêu ---
import argparse
import datetime
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.json"
TODAY = datetime.date.today()
YEAR = TODAY.strftime("%Y")
MONTH = TODAY.strftime("%m")

PROBLEMS_ROOT = ROOT / "problems"

TEMPLATE = '''"""
Title: {title}
ID: {id}
Tags: {tags}
Difficulty: {difficulty}
Link: {link}
Time: TBD
Space: TBD
"""
class Solution:
    def solve(self, *args, **kwargs):
        # TODO: implement
        pass
'''

# import theo tên module (đÃ thay '-' -> '_')
TEST_TEMPLATE = """from problems.y{year}.m{month}.{module_name} import Solution

def test_sample():
    s = Solution()
    # TODO: replace with real assertions
    assert True
"""


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def moduleize(slug: str) -> str:
    # module/file name: chỉ a-z0-9 và '_' (an toàn tuyệt đối cho import)
    return re.sub(r"[^a-z0-9]+", "_", slug)


def ensure_package(path: pathlib.Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    initf = path / "__init__.py"
    if not initf.exists():
        initf.write_text("# package\n")


def read_index():
    if not INDEX.exists():
        return {"started": str(TODAY), "problems": []}
    try:
        raw = INDEX.read_text(encoding="utf-8").strip()
        if not raw:
            return {"started": str(TODAY), "problems": []}
        data = json.loads(raw)
        data.setdefault("started", str(TODAY))
        data.setdefault("problems", [])
        return data
    except Exception:
        return {"started": str(TODAY), "problems": []}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("title", help="problem title or slug")
    ap.add_argument("--id", type=str, default="")
    ap.add_argument("--tags", type=str, default="")
    ap.add_argument("--difficulty", type=str, default="unknown")
    ap.add_argument("--link", type=str, default="")
    args = ap.parse_args()

    slug = slugify(args.title)  # hiển thị/README
    module_slug = moduleize(slug)  # dùng cho TÊN FILE/MODULE
    year_pkg = f"y{YEAR}"
    month_pkg = f"m{MONTH}"

    # đảm bảo packages tồn tại
    ensure_package(PROBLEMS_ROOT)
    ensure_package(PROBLEMS_ROOT / year_pkg)
    dir_path = PROBLEMS_ROOT / year_pkg / month_pkg
    ensure_package(dir_path)

    # tên file solution + test đều dùng module_slug (không có '-')
    fname = f"lc{args.id}_{module_slug}.py" if args.id else f"{module_slug}.py"
    fpath = dir_path / fname
    test_name = f"test_{module_slug}.py"

    # viết file solution
    fpath.write_text(
        TEMPLATE.format(
            title=args.title,
            id=args.id or "N/A",
            tags=args.tags or "N/A",
            difficulty=args.difficulty,
            link=args.link or "N/A",
        ),
        encoding="utf-8",
    )

    # viết file test (import theo module_name an toàn)
    tests = ROOT / "tests"
    tests.mkdir(exist_ok=True)
    (tests / test_name).write_text(
        TEST_TEMPLATE.format(year=YEAR, month=MONTH, module_name=fpath.stem),
        encoding="utf-8",
    )

    # cập nhật index.json
    data = read_index()
    entry = {
        "date": str(TODAY),
        "year": YEAR,
        "month": MONTH,
        "id": args.id,
        "title": args.title,
        "slug": slug,  # giữ slug đẹp để hiển thị
        "file": f"problems/{year_pkg}/{month_pkg}/{fname}",
        "test": f"tests/{test_name}",
        "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
        "difficulty": args.difficulty,
        "link": args.link,
        "status": "done",
        "opt_rounds": 0,
    }
    data.setdefault("problems", []).append(entry)
    INDEX.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print(f"Created: {fpath}")
    print(f"Created: {tests / test_name}")
    print("index.json updated.")


if __name__ == "__main__":
    main()
