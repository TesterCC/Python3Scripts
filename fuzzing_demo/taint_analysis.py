# demo from gpt
'''
污点分析是一种在程序分析中用于跟踪和监控特定数据（称为污点数据）在程序中的传播和使用的技术。
它常用于检测和预防诸如代码注入、跨站脚本攻击等安全漏洞。
以下是一个使用 Python 实现简单污点分析的示例代码，用于跟踪用户输入在程序中的传播
在以下示例中，将用户输入视为污点数据，然后跟踪它经过一系列操作后的变化。

污点分析的原理主要基于对程序中数据的标记和跟踪。
首先，确定哪些数据被视为“污点源”，例如用户输入、从不可信的外部来源获取的数据等。这些数据被标记为“污点”。
然后，在程序执行过程中，跟踪污点数据的传播。这包括通过变量赋值、函数调用参数传递、数据计算和操作等方式的传播。
通过分析程序的控制流和数据流，确定污点数据是否能够到达关键的操作或敏感的位置，比如数据库操作、文件写入、网络发送等。
如果污点数据能够到达这些可能导致安全风险的位置，就意味着可能存在安全漏洞。
例如，如果用户输入的污点数据未经充分验证就被用于构造数据库查询语句，可能导致 SQL 注入攻击。
'''

def taint_analysis(user_input):
    tainted = [user_input]
    operations = [
        lambda x: x + " added",   # tainted operation 1
        lambda x: x * 2           # tainted operation 2
    ]

    for op in operations:
        new_tainted = []
        for t in tainted:
            result = op(t)
            new_tainted.append(result)
            print(f"Operation: {op.__name__}, Input: {t}, Result: {result}")
        tainted.extend(new_tainted)

user_input = "user_data"
taint_analysis(user_input)