import os
from PyPDF2 import PdfReader, PdfWriter

# pip install PyPDF2 -i https://pypi.tuna.tsinghua.edu.cn/simple
# 需求：将大文件拆分为小于10M的多个pdf（非精准切分）

# 指定输入PDF文件路径
input_file = "test20230817.pdf"

# 指定输出目录
output_directory = "output"

# 指定拆分后的最大文件大小（以字节为单位）
max_file_size = 9 * 1024 * 1024  # 10MB


def split_pdf(input_path, output_dir, max_size):
    # 读取输入PDF文件
    pdf = PdfReader(input_path)

    # 获取PDF的总页数
    total_pages = len(pdf.pages)

    # PDF的切分，文件总大小除9M(要切分的大小)就是平均切分数，再向上取整为一个实际份数。如果分出来的还是超过目标，增加切分份数。
    file_size = os.path.getsize(input_path)

    delta_num = 3

    # 平均分成多少份 = 计算的平均值向上取整 + 以防集中page过大的附加页数
    num_files = round(file_size / max_size) + delta_num

    # 每一个
    max_pages = total_pages // num_files

    # 能切分，就是算法有点问题
    # num_files = (total_pages // max_pages) + 1
    print(f"[D]total_pages:{total_pages}, max_pages: {max_pages}, nums: {num_files}")

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 拆分PDF文件
    for i in range(num_files):
        # 创建一个新的PDF写入对象
        output_pdf = PdfWriter()

        # 确定当前文件的起始和结束页码
        start_page = i * max_pages
        end_page = min((i + 1) * max_pages, total_pages)

        # 将指定页范围的内容添加到新的PDF文件中
        for page in range(start_page, end_page):
            # output_pdf.addPage(pdf.getPage(page))
            output_pdf.add_page(pdf.pages[page])

        # 构造输出文件路径
        output_file = os.path.join(output_dir, f"output_{i + 1}.pdf")

        # 将拆分后的PDF文件保存到输出路径
        with open(output_file, "wb") as f:
            output_pdf.write(f)

        print(f"拆分完成：{output_file}")


# 调用拆分PDF函数
split_pdf(input_file, output_directory, max_file_size)
