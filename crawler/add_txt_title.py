import re

change_file_path = "question_with_answer_v2.md"

def modify_text(text):
    # 定义一个正则表达式模式，用于匹配标题行
    # ^ 表示匹配行的开头
    # (\d+\.\s*.+) 是一个捕获组，用于捕获标题内容
    # \d+ 匹配一个或多个数字，代表标题序号
    # \. 匹配点号
    # \s* 匹配零个或多个空白字符
    # .+ 匹配一个或多个任意字符，代表标题的具体内容
    # $ 表示匹配行的结尾
    pattern = r'^(\d+\.\s*.+)$'

    # 使用 re.sub 函数进行替换操作
    # 第一个参数是正则表达式模式
    # 第二个参数是替换的字符串，r'## \1' 表示在匹配到的标题前加上 '## '
    # \1 是反向引用，代表正则表达式中的第一个捕获组，即匹配到的标题内容
    # 第三个参数是要处理的文本
    # flags=re.M 表示使用多行模式，使得 ^ 和 $ 可以匹配每行的开头和结尾
    new_text = re.sub(pattern, r'## \1', text, flags=re.M)
    return new_text


# 读取 txt 文件内容, 以只读模式打开文件，并指定编码为 utf-8
with open(change_file_path, 'r', encoding='utf-8') as file:
    # 读取文件的全部内容
    content = file.read()

print("----------handle txt----------")
# 修改文本
modified_content = modify_text(content)

# 将修改后的内容写回文件
with open(change_file_path, 'w', encoding='utf-8') as file:
    # 将修改后的内容写回文件
    file.write(modified_content)

print("---Fin---")