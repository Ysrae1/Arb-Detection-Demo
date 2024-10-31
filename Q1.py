from lib import ArbDataStruct as arb
from lib import TradingPairs as tp
import threading
import time
import os
import sys

def session(event, trading_pairs, exchange_rates, cycles, heap, update_interval, start_time):
    best_cycle_counter = 0  # 最优路径变动次数
    previous_best_cycle = None  # 上一次的最优回路

    while True:
        event.wait()  # 等待开始信号

        # 移动光标到第二行第一列
        print('\033[2;1H', end='')

        # 清除从光标到屏幕末尾的内容
        print('\033[J', end='')

        # 计算程序已运行的持续时间
        elapsed_time = time.time() - start_time
        elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

        # 打印标题信息
        print("套利检测程序正在运行...")
        print(f"开始时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
        print(f"持续时间：{elapsed_time_str}")
        print(f"最优路径变动次数：{best_cycle_counter}\n")

        # 模拟实时更新
        print("模拟实时更新交易对：")
        updated_indices = tp.update(trading_pairs, num_updates=5, min_rate=0.5, max_rate=1.5)

        # 更新受影响的回路
        print("更新受影响的回路...")
        update_start_time = time.time()  # 开始计时
        affected_cycles = set()
        for idx in updated_indices:
            a, b, rate = trading_pairs[idx]
            edge = (a, b)
            exchange_rates[edge] = rate
            # 找到包含该边的所有回路
            for cycle in cycles:
                if edge in cycle:
                    affected_cycles.add(cycle)
        arb.update_heap(heap, affected_cycles, exchange_rates)
        update_end_time = time.time()  # 结束计时
        update_elapsed_time = update_end_time - update_start_time
        print(f"更新受影响的回路耗时：{update_elapsed_time:.6f} 秒")

        # 获取最盈利的回路
        get_best_start_time = time.time()  # 开始计时
        if heap:
            profit, best_cycle = heap[0]
            # 检查最优回路是否发生变化
            if best_cycle != previous_best_cycle:
                best_cycle_counter += 1
                previous_best_cycle = best_cycle
            print(f"最盈利的回路：{best_cycle}，盈利：{-profit}")
        else:
            print("未找到回路")
        get_best_end_time = time.time()  # 结束计时
        get_best_elapsed_time = get_best_end_time - get_best_start_time
        print(f"获取最盈利的回路耗时：{get_best_elapsed_time:.6f} 秒")

        time.sleep(update_interval)
        if not event.is_set():
            # 移动光标到第二行第一列并清除内容
            print('\033[2;1H', end='')
            print('\033[J', end='')
            print("检测到停止指令，暂停更新。\n")
            event.wait()  # 再次等待开始信号

def listen_for_commands(event):
    while True:
        # 移动光标到第一行第一列
        print('\033[1;1H', end='')
        # 清除当前行
        print('\033[2K', end='')
        # 根据当前状态显示提示信息
        if event.is_set():
            print("输入 's' 停止，'e' 退出：", end='', flush=True)
        else:
            print("输入 's' 开始，'e' 退出：", end='', flush=True)
        # 获取用户输入
        command = input().strip().lower()
        if command == 's':
            if event.is_set():
                event.clear()
                print("已发送停止指令，等待当前循环结束后停止。\n")
            else:
                event.set()
                print("开始更新和检测套利机会。\n")
        elif command == 'e':
            print("退出程序。")
            event.clear()
            break
        else:
            print("无效的指令，请输入 's' 或 'e'。\n")

def main():
    # 生成交易对
    trading_pairs = tp.generator(num_pairs=500, num_assets=50, min_rate=0.5, max_rate=1.5, seed=42)

    # 构建交易图和交换比例
    graph, exchange_rates = arb.build_graph(trading_pairs)

    # 限制回路长度
    max_length = 4

    # 找到所有回路
    print("查找回路中...")
    cycles = arb.find_cycles(graph, max_length)
    print(f"找到 {len(cycles)} 个回路")

    # 构建最大堆
    print("构建最大堆...")
    heap = arb.build_heap(cycles, exchange_rates)

    # 定义更新的时间间隔（秒）
    update_interval = 0.05  # 可以根据需要调整

    # 记录程序开始时间
    start_time = time.time()

    # 创建一个 Event 对象，用于线程间通信
    event = threading.Event()
    event.clear()  # 初始状态为未设置，即停止状态

    # 清除屏幕并移动光标到左上角
    print('\033[2J\033[H', end='')

    # 创建并启动更新和检测的线程
    update_thread = threading.Thread(target=session, args=(event, trading_pairs, exchange_rates, cycles, heap, update_interval, start_time))
    update_thread.daemon = True  # 设置为守护线程
    update_thread.start()

    # 创建并启动监听用户输入的线程
    command_thread = threading.Thread(target=listen_for_commands, args=(event,))
    command_thread.daemon = True
    command_thread.start()

    # 主线程等待命令线程结束
    command_thread.join()
    print("程序已退出。")

if __name__ == "__main__":
    main()