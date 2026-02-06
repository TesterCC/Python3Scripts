# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/3


def get_physical_memory_gb(default_gb: int = 8) -> int:
    """
    读取物理内存（GiB），向下取整
    失败时返回 default_gb（保守兜底）
    """
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    kb = int(line.split()[1])
                    return kb // (1024 * 1024)
    except Exception:
        pass

    return default_gb


CONCURRENCY_TABLE = [
    (8, 2),  # 8G
    (16, 4),  # 16G   # 实测5个并发比较危险，4个并发要安全些
    (32, 11),  # 32G
    (64, 23),  # 64G
]


def get_safe_opengrep_concurrency(
        default_mem_gb: int = 8,
) -> int:
    """
    根据物理内存返回安全的 opengrep scan 并发数

    前提：
      - --jobs = 1
      - --max-memory = 1024
    """

    mem_gb = get_physical_memory_gb(default_mem_gb)

    # 向下匹配并发档位（保守策略）
    for threshold, concurrency in CONCURRENCY_TABLE:
        if mem_gb < threshold:
            return concurrency

    # >= 最大档位（64G 及以上）
    return CONCURRENCY_TABLE[-1][1]


if __name__ == '__main__':
    print(get_safe_opengrep_concurrency())
