import os
import sys

# Tự động biên tập source code theo quy định ...
# Các thư mục cần bỏ qua
IGNORE_DIRS = {
    ".git",
    "node_modules",
    "venv",
    ".venv",
    "env",
    "__pycache__",
    "dist",
    "build",
    "target",
    ".next",
    ".idea",
    ".vscode",
}

# Các file cần bỏ qua tuyệt đối (bảo mật & file rác)
IGNORE_FILES = {
    ".DS_Store",
    ".env",
    ".env.local",
    ".env.production",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "Podfile.lock",
}

# Phần mở rộng file mã nguồn chính (bạn có thể thêm bớt tùy dự án)
CODE_EXTS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".kt",
    ".swift",
    ".c",
    ".cpp",
    ".cc",
    ".h",
    ".hpp",
    ".cs",
    ".go",
    ".rs",
    ".php",
    ".rb",
    ".html",
    ".css",
    ".scss",
    ".sql",
    ".sh",
    ".yaml",
    ".yml",
    ".json",
    ".md",
}


def collect_code(project_dir: str, output_txt: str):
    project_dir = os.path.abspath(project_dir)
    if not os.path.isdir(project_dir):
        print(f"Lỗi: Không tìm thấy thư mục '{project_dir}'")
        return

    file_count = 0
    total_lines = 0

    with open(output_txt, "w", encoding="utf-8") as out:
        out.write(f"SOURCE CODE EXPORT - PROJECT: {os.path.basename(project_dir)}\n")
        out.write("=" * 80 + "\n\n")

        for root, dirs, files in os.walk(project_dir):
            # Lọc bỏ các thư mục không mong muốn ngay khi duyệt
            dirs[:] = sorted(d for d in dirs if d not in IGNORE_DIRS)

            for fname in sorted(files):
                if fname in IGNORE_FILES or fname.startswith(".env"):
                    continue

                ext = os.path.splitext(fname)[1].lower()
                if ext not in CODE_EXTS:
                    continue

                full_path = os.path.join(root, fname)
                rel_path = os.path.relpath(full_path, project_dir)

                # Tránh đọc lại chính file output nếu nằm cùng thư mục
                if os.path.abspath(full_path) == os.path.abspath(output_txt):
                    continue

                try:
                    with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                        lines = f.readlines()
                except Exception as e:
                    print(f"Bỏ qua file lỗi đọc {rel_path}: {e}")
                    continue

                file_count += 1
                total_lines += len(lines)

                out.write(f"\n{'=' * 80}\n")
                out.write(f"FILE #{file_count}: {rel_path} ({len(lines)} lines)\n")
                out.write(f"{'=' * 80}\n\n")

                for idx, line in enumerate(lines, start=1):
                    out.write(f"{idx:4d} | {line}")

                out.write("\n")

    print(f"Xong! Đã gom {file_count} file ({total_lines} dòng) vào: {output_txt}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python3 gom_code.py /đường/dẫn/tới/thư_mục_dự_án [file_đầu_ra.txt]")
        sys.exit(1)

    target_dir = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) >= 3 else "source_code_ban_in.txt"
    collect_code(target_dir, out_file)