[//]: # (Logo)

# Dự án Từ điển thuật ngữ AI dành cho người Việt

<!-- ![GitHub repo size](https://img.shields.io/github/repo-size/aidic-org-ebook/ai-dictionary-ebook?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/aidic-org-ebook/ai-dictionary-ebook?color=%233a87f2&label=contributors&style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/aidic-org-ebook/ai-dictionary-ebook?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/aidic-org-ebook/ai-dictionary-ebook?color=%23f2af3a&style=flat-square) -->

* https://aidic.org/
* https://dic4ai.org/

Dự án có thể chia thành nhiều giai đoạn nhỏ để xử lý, nhưng nhìn chung thì sẽ có hai giai đoạn chính:
- **Giai đoạn 1: Tìm từ** trong dự án Từ điển thuật ngữ AI dành cho người Việt. Đây là giai đoạn cần được thực hiện liên tục, các thành viên chính thức trong dự án và những cá nhân khác muốn đóng góp được khuyến khích tham gia giai đoạn này trước tiên để có thể xây dựng được một cơ sở dữ liệu các thuật ngữ phổ biến đủ lớn dành cho Giai đoạn 2.
- **Giai đoạn 2: Dịch từ**. Trong giai đoạn này, lần lượt các từ đã qua Giai đoạn 1 sẽ được giao cho từng thành viên để dịch, với mục tiêu là giải thích một cách dễ hiểu ý nghĩa của thuật ngữ, giúp người đọc hiểu được thuật ngữ trong ngữ cảnh ML và AI, hình dung được cách sử dụng từ qua ví dụ và hình minh hoạ.

## Cấu trúc thư mục
- Thư mục `collections`: chứa dữ liệu của dữ án được lưu theo định dạng JSON, gồm các tệp `A.json`, `B.json` , ... `Z.json` chia các từ theo bảng chữ cái. Các thành viên tham gia đóng góp đa phần sẽ tương tác với thư mục này.
- Thư mục `ebook`: chứa chứa template Ebook viết bằng Latex, trong đó:
    - Tệp `ai-dictionary-ebook.tex` sử dụng để build bản PDF
    - Thư mục `chapter` chứa toàn bộ bản dịch của cuốn Từ điển thuật ngữ AI dành cho người Việt, và được chia thành các tệp `A.tex`, `B.tex`, ... , `Z.tex` theo bảng chữ cái.
    - Tệp `reference.bib` chứa tài liệu tham khảo của cuốn Từ điển dưới dạng BibTeX.
- Thu mục `utils`: chứa các hàm Python hỗ trợ tự động hoá các bước chuyển đổi giữa các dạng dữ liệu trong dự án (JSON, Latex, Markdown, ...).
- Thư mục `docs`: chứa các tài liệu hướng dẫn của kho chứa này.

## Đóng góp cho dự án Từ điển
Để tham gia đóng góp cho dự án Từ điển thuật ngữ AI dành cho người Việt, bạn có thể:
- Đề xuất thêm từ mới vào kho thuật ngữ của dự án hoặc tham gia dịch thuật thông qua các Pull Request theo các bước theo Hướng dẫn dịch thuật **[tại đây](docs/CONTRIBUTING.md)**.
- Tham gia phản biện (review) các Pull Request theo Hướng dẫn dành cho người phản biện **[tại đây](docs/REVIEWER_INSTRUCTION.md)**.
- Đề xuất chỉnh sửa về ngữ pháp, những điểm chưa nhất quán trong cách dịch.
- Sửa các lỗi chính tả trong bản thảo.
- Hỗ trợ kỹ thuật.
- Star github repo của dự án.
- Chia sẻ dự án tới nhiều người hơn.

Mọi đề xuất bổ sung và chỉnh sửa nội dung của cuốn Từ điển thuật ngữ AI dành cho người Việt đều được hoan nghênh.

## Thảo luận cùng nhóm Dịch thuật
Bạn có thể bắt đầu một cuộc thảo luận mới **[tại đây](https://github.com/aidic-org-ebook/ai-dictionary-ebook/discussions)**.

## Lời cảm ơn
Bằng sự  sâu sắc, nhóm điều hành dự án trân trọng gửi lời cảm ơn và tri ân đến những người đã đóng góp vào dự án này dù ít hay nhiều.

Những đóng góp cụ thể của Cộng đồng được chúng tôi liệt kê đầy đủ **[tại đây](ACKNOWLEDGEMENT.md)**.

## Maintainers
* Trần Quang Huy [@huyquangtranaus](https://github.com/huyquangtranaus)
* Đỗ Trường Giang [@trGiang99](https://github.com/trGiang99)

[//]: # (Giấy phép)
