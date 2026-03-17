Bài tập 1: Tạo cây thư mục và quản lý file cơ bản
Bạn được cung cấp một danh sách các đường dẫn file và thư mục. Mỗi đường dẫn trên một dòng. File có phần mở rộng (ví dụ: .txt, .py), thư mục không có phần mở rộng. Hãy đếm số lượng file và số lượng thư mục.

Đầu vào:

Dòng đầu tiên chứa số nguyên n (1 ≤ n ≤ 1000) là số lượng đường dẫn.

n dòng tiếp theo, mỗi dòng chứa một đường dẫn (chỉ chứa chữ cái, số, dấu chấm, dấu gạch chéo, không có khoảng trắng, độ dài ≤ 100).

Đầu ra:

In ra hai số nguyên: số lượng file và số lượng thư mục, cách nhau bởi một khoảng trắng.

Ví dụ: Đầu vào: 5 /home/user file.txt folder script.py README

Đầu ra: 2 3

Giải thích: file.txt và script.py là file (có .txt và .py), các đường dẫn còn lại là thư mục.

Lưu ý: Đầu ra trong test cases sử dụng văn bản không dấu để tránh lỗi kỹ thuật.

Test Cases Mẫu (1 hiển thị / 1 tổng)



Bạn có thể test với 1 test case(s) mẫu. Code của bạn sẽ được đánh giá với tất cả 1 test cases (bao gồm 0 test cases ẩn).

Ví dụ 1

Mẫu: 2 file (file.txt, script.py) và 3 thư mục (/home/user, folder, README).

Đầu vào:

5

/home/user

file.txt

folder

script.py

README

Đầu ra:

2 3
