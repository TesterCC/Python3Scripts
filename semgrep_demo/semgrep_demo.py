import subprocess
import json
import os

project_root = os.path.dirname(os.path.abspath(__file__))
print(f"[D] project_root path is: {project_root}")

def detect_language_by_extension(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension in ['.py']:
        return 'Python'
    elif file_extension in ['.js', '.jsx']:
        return 'JavaScript'
    elif file_extension in ['.ts', '.tsx']:
        return 'TypeScript'
    elif file_extension in ['.java']:
        return 'Java'
    elif file_extension in ['.go']:
        return 'Go'
    elif file_extension in ['.cpp', '.cc', '.cxx', '.c']:
        return 'C/C++'
    elif file_extension in ['.rb']:
        return 'Ruby'
    elif file_extension in ['.php']:
        return 'PHP'
    elif file_extension in ['.rs']:
        return 'Rust'
    elif file_extension in ['.cs']:
        return 'C#'
    elif file_extension in ['.html', '.htm']:
        return 'HTML'
    elif file_extension in ['.css']:
        return 'CSS'
    elif file_extension in ['.swift']:
        return 'Swift'
    else:
        return 'Unknown Languages, please check file.'

def remove_existing_json(json_file):
    # check and delete exist semgrep.json
    if os.path.exists(json_file):
        os.remove(json_file)
        print(f"{json_file} deleted")
    else:
        print(f"{json_file} is not exist")

def run_semgrep(scan_path, json_file):

    # check path and output result file
    if not os.path.exists(scan_path):
        print(f"scan path {scan_path} is not exist, please check it.")
        return

    scan_path_parent = os.path.dirname(scan_path)
    print(f"[D] scan_path: {scan_path}")
    print(f"[D] scan_path_parent: {scan_path_parent}")

    output_result_path = f"{scan_path_parent}/result"
    os.makedirs(output_result_path,exist_ok=True)

    # Build semgrep scan command; attention don't use shell=True, it will cause security issue.
    command = ['semgrep', 'scan',  '--metrics=off', '--config', f'{scan_path_parent}/semgrep-rules0/', '--json', f'--json-output={output_result_path}/{json_file}', scan_path]
    command_str = ' '.join(command)
    print(f"shell command: {command_str}")


    try:
        # subprocess.run(command, check=True)
        subprocess.run(command)
        print(f"Semgrep scan finish, the result saved at {json_file}")
    except subprocess.CalledProcessError as e:
        print(f"Semgrep run error: {e}")

def parse_semgrep_json(json_file):
    # 读取 semgrep.json 文件
    if not os.path.exists(json_file):
        print(f"JSON 文件 {json_file} 不存在。")
        return

    with open(json_file, 'r', encoding='utf-8') as f:
        semgrep_result = json.load(f)
    
    # parse results
    findings = semgrep_result.get('results', [])
    if not findings:
        print("没有发现任何结果。")
        return

    for finding in findings:
        # 获取路径、漏洞类型、描述和语言
        path = finding.get('path', '未知文件')
        start_line = finding.get('start', {}).get('line', '未知行')
        vuln_type = finding.get('extra', {}).get('metadata', {}).get('category', '未知类型')
        message = finding.get('extra', {}).get('message', '无描述')
        severity = finding.get('extra', {}).get('severity', '未定义严重性')

        cwe_info_list = finding.get('extra', {}).get('metadata', {}).get('cwe', [])
        cwe_info = ""
        if len(cwe_info_list) > 0:
            cwe_info = cwe_info_list[0]

        owasp_info_list = finding.get('extra', {}).get('metadata', {}).get('owasp', [])
        if len(owasp_info_list) > 0:
            owasp_info = owasp_info_list[0]

        ref_list = finding.get('extra', {}).get('metadata', {}).get('references')



        # 打印信息
        # 根据文件路径后缀判断语言类型
        lang = detect_language_by_extension(path)

        print(f"文件: {path}, 行号: {start_line}, 严重性: {severity}")
        print(f"漏洞类型: {vuln_type}") 
        print(f"描述: {message}")
        print(f"语言: {lang}")
        print(f"CWE信息: {cwe_info}")
        print(f"OWASP信息: {owasp_info}")
        print(f"参考链接: {ref_list}")
        print("-" * 66)


if __name__ == '__main__':
    # # check code
    # json_file = 'semgrep_result_temp.json'
    #
    # # remove old semgrep.json
    # remove_existing_json(json_file)
    #
    # # scan_path = input("please input the path of your scan: ")  # origin
    # scan_path = "/opt/static_code_checker/sample0"
    #
    # run_semgrep(scan_path, json_file)

    # parse result

    # test result parse
    json_file = 'sresult1.json'
    parse_semgrep_json(f"./result/{json_file}")
