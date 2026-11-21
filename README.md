# Công Cụ Gom Mã Nguồn Phục Vụ Hồ Sơ Đăng Ký Bản Quyền Phần Mềm

Script Python (`gom_code.py`) hỗ trợ quét thư mục dự án, lọc bỏ thư mục thư viện/file rác/file cấu hình nhạy cảm, đánh số dòng và xuất toàn bộ mã nguồn ra một file `.txt` thống nhất để chuẩn bị định dạng và in ấn nộp hồ sơ đăng ký quyền tác giả chương trình máy tính.

---

## 1. Yêu cầu hệ thống

* **Hệ điều hành:** macOS.
* **Python:** Phiên bản **Python 3.8 trở lên** (macOS thường đã cài sẵn `python3` hoặc có thể cài qua Homebrew).

Kiểm tra nhanh phiên bản Python trong Terminal:

```bash
python3 --version
```

Nếu chưa có hoặc muốn cài mới qua Homebrew:

```bash
brew install python
```

---

## 2. Cấu trúc thư mục gợi ý

Đặt script và file hướng dẫn tại một vị trí thuận tiện, ví dụ trên **Desktop**:

```text
~/Desktop/
├── gom_code.py
└── README.md
```

---

## 3. Cách thiết lập (`Setup`)

1. Mở ứng dụng **Terminal** trên macOS (`Cmd + Space`, gõ `Terminal`, nhấn `Enter`).
2. Di chuyển tới thư mục chứa script (ví dụ `Desktop`):

```bash
cd ~/Desktop
```

3. Tạo file `gom_code.py` và dán mã nguồn Python vào (hoặc dùng `nano gom_code.py`, dán code, nhấn `Ctrl + O` để lưu, `Ctrl + X` để thoát):

```bash
nano gom_code.py
```

4. Kiểm tra script chạy được:

```bash
python3 gom_code.py
```

Nếu màn hình hiển thị dòng hướng dẫn `Cách dùng: python3 gom_code.py ...` là đã sẵn sàng.

---

## 4. Cách chạy script

### Cú pháp cơ bản

```bash
python3 /đường/dẫn/tới/gom_code.py /đường/dẫn/tới/thư_mục_dự_án [file_đầu_ra.txt]
```

* Tham số 1 (bắt buộc): Đường dẫn thư mục dự án cần gom code.
* Tham số 2 (tùy chọn): Đường dẫn/tên file `.txt` xuất ra. Nếu bỏ qua, mặc định tạo file `source_code_ban_in.txt` tại thư mục làm việc hiện tại.

### Ví dụ thực tế

Giả sử dự án nằm tại `~/Projects/my-app` và bạn muốn xuất file ra `~/Desktop/source_code_ban_in.txt`:

```bash
python3 ~/Desktop/gom_code.py ~/Projects/my-app ~/Desktop/source_code_ban_in.txt
```

**Mẹo thao tác nhanh trên macOS:**
Gõ `python3 ~/Desktop/gom_code.py ` (có dấu cách ở cuối), sau đó **kéo thả thư mục dự án** từ Finder vào cửa sổ Terminal để tự động điền chuẩn đường dẫn có dấu cách hoặc ký tự tiếng Việt, rồi gõ thêm đường dẫn file xuất ra và nhấn `Enter`.

---

## 5. Tùy chỉnh bộ lọc trước khi chạy

Mở `gom_code.py` bằng trình soạn thảo văn bản nếu cần điều chỉnh các danh sách sau:

* **`IGNORE_DIRS`**: Các thư mục bị bỏ qua hoàn toàn (mặc định gồm `.git`, `node_modules`, `venv`, `.venv`, `__pycache__`, `dist`, `build`, `target`, `.next`, `.idea`, `.vscode`...). Có thể thêm thư mục sinh tự động của framework/ngôn ngữ riêng.
* **`IGNORE_FILES`**: Các file bị loại bỏ để tránh lộ thông tin bảo mật hoặc file khóa/rác (mặc định gồm `.DS_Store`, `.env`, `.env.local`, `.env.production`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `Podfile.lock`...).
* **`CODE_EXTS`**: Danh sách đuôi file mã nguồn sẽ được thu thập (`.py`, `.js`, `.ts`, `.tsx`, `.java`, `.cpp`, `.c`, `.h`, `.html`, `.css`, `.sql`, `.json`, `.md`...). Bổ sung thêm đuôi file nếu dự án dùng ngôn ngữ/định dạng đặc thù.

---

## 6. Lưu ý sau khi xuất file trước khi đem in

1. **Rà soát bảo mật lần cuối:** Mở file `.txt` vừa xuất và kiểm tra xem có API key, secret token, chuỗi kết nối CSDL hay mật khẩu nào bị viết cứng (hardcode) trong mã nguồn không.
2. **Định dạng & chia trang theo quy chuẩn:**
   * Mở file `.txt` bằng **Pages**, **Microsoft Word** hoặc **Google Docs**.
   * Dùng font monospace (`Menlo`, `Monaco` hoặc `Courier New`), cỡ chữ vừa phải (khoảng `9pt–10pt`) để trình bày rõ ràng, bật đánh số trang.
   * **Dưới 100 trang:** In toàn bộ.
   * **Từ 100 trang trở lên:** Tách in **25 trang đầu – 25 trang giữa – 25 trang cuối**, đóng quyển và ký nháy/đóng dấu giáp lai theo quy định hồ sơ.
