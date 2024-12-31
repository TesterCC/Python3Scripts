# coding=utf-8
import ast
import os


def main():
    input_path = os.path.abspath(os.curdir)
    file_name = os.path.join(input_path, 'simple_ast_demo.py')
    with open(file_name, "r", encoding="utf-8") as f:
        contents = f.read()
    try:
        tree = ast.parse(contents)
        print("obj type: ")
        print(type(tree))
    finally:
        print("END")


if __name__ == '__main__':
    main()
