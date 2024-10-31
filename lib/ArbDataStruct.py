import heapq
from collections import defaultdict

def build_graph(trading_pairs):
    graph = defaultdict(list)
    exchange_rates = {}
    for a, b, rate in trading_pairs:
        graph[a].append(b)
        exchange_rates[(a, b)] = rate
    return graph, exchange_rates

def find_cycles(graph, max_length):
    cycles = []
    def dfs(start, current, path, visited):
        if len(path) > max_length:
            return
        if current == start and len(path) > 0:
            cycles.append(tuple(path.copy()))  # 将回路转换为元组
            return
        for neighbor in graph[current]:
            if neighbor not in visited or neighbor == start:
                visited.add(neighbor)
                path.append((current, neighbor))
                dfs(start, neighbor, path, visited)
                path.pop()
                visited.remove(neighbor)
    for node in graph:
        dfs(node, node, [], set([node]))
    return cycles

def calculate_profit(cycle, exchange_rates):
    profit = 0
    total_rate = 1
    for edge in cycle:
        rate = exchange_rates[edge]
        total_rate *= rate
    profit = total_rate - 1
    return profit

def build_heap(cycles, exchange_rates):
    heap = []
    for cycle in cycles:
        profit = calculate_profit(cycle, exchange_rates)
        heapq.heappush(heap, (-profit, cycle))
    return heap

def update_heap(heap, affected_cycles, exchange_rates):
    for i in range(len(heap)):
        profit, cycle = heap[i]
        if cycle in affected_cycles:
            new_profit = calculate_profit(cycle, exchange_rates)
            heap[i] = (-new_profit, cycle)
    heapq.heapify(heap)