# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/6


import json
import pymysql


# ====== 数据库配置 ======
DB_CONFIG = {
    "host": "10.29.xx.xx",
    "port": 33306,
    "user": "root",
    "password": "xxxx",
    "database": "fwas",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": False,   # 显式提交，防误操作
}


# JSON_FILE = "data/260206-handle-data-small-cleaned.json"  # MVP TEST
JSON_FILE = "data/260206-handle-data-cleaned.json"


UPDATE_SQL = """
UPDATE t_srcsec_rules
SET rule_content = %s
WHERE id = %s
"""


def main():
    # 1. 读取 JSON
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        rules = json.load(f)

    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()

    success = 0
    not_found = 0

    try:
        for item in rules:
            rule_id = item.get("id")
            rule_content = item.get("rule_content")

            if rule_id is None or rule_content is None:
                print(f"[SKIP] invalid item: {item}")
                continue

            cursor.execute(UPDATE_SQL, (rule_content, rule_id))

            if cursor.rowcount == 0:
                not_found += 1
                print(f"[MISS] id not found: {rule_id}")
            else:
                success += 1
                print(f"[OK] updated id={rule_id}")

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()

    print("\n====== SUMMARY ======")
    print(f"Updated:   {success}")
    print(f"Not Found: {not_found}")


if __name__ == "__main__":
    main()
