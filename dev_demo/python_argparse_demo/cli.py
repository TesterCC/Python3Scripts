# coding:utf-8
import json
import argparse
import traceback
import textwrap


def print_args(dir, path, task_id=None):
    code, msg, data = None, "", {}

    if dir and path and task_id:
        code = 1
        msg = "success"
        data = {"task_id": task_id, "dir": dir, "path": path}
    else:
        code = 500
        msg = "internal error"

    ret = {
        "code": code,
        "msg": msg,
        "data": data
    }

    ret_json_str = json.dumps(ret)

    #     print(f"[D] ret_json_str: {ret_json_str}")   # only debug use
    return ret_json_str


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="CLI Test Demo",
                                         formatter_class=argparse.RawDescriptionHelpFormatter,
                                         epilog=textwrap.dedent('''Example:
        python cli.py -h
        python cli.py -i 1 -d /opt/a -f /opt/b.bin
        '''
        ))
        parser.add_argument('-i', '--task_id', type=int, help='execute task id')
        parser.add_argument("-d", "--all", type=str, default="", help="all dir absolute path")
        parser.add_argument("-f", "--single_file", type=str, default="", help="single file absolute path")

        args = parser.parse_args()
        #         print(f"parser args: {parser}")  # only debug use
        if args.task_id and args.all and args.single_file:
            resp = print_args(args.all, args.single_file, task_id=args.task_id)
            print(resp)

    except Exception as e:
        traceback.format_exc()
