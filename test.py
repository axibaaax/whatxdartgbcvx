import math

import ray
import time

# 初始化 Ray
ray.init(ignore_reinit_error=True)

# 定义并行任务
@ray.remote


def parallel_task():
    start_time = time.time()
    # 模拟复杂的浮点数运算
    result = 0
    for i in range(1, 10**7):
        result += math.sqrt(i)
    end_time = time.time()
    return end_time - start_time


# def parallel_task():
#     start_time = time.time()
#     time.sleep(5)  # 模拟需要执行5秒的操作
#     end_time = time.time()
#     return end_time - start_time


def main():
    try:
        # 启动5个并行任务
        tasks = [parallel_task.remote() for _ in range(45)]

        # 获取每个任务的执行时间
        execution_times = ray.get(tasks)

        # 打印每个任务的执行时间
        for i, time_taken in enumerate(execution_times):
            print(f"Task {i + 1}: {time_taken:.8f} seconds")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 关闭 Ray
        ray.shutdown()

if __name__ == "__main__":
    main()
