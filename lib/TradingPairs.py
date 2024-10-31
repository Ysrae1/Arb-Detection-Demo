import random

def generator(num_pairs=50000, num_assets=5000, min_rate=0.5, max_rate=1.5, seed=None):
    """
    生成指定数量的交易对。

    参数：
    - num_pairs: 要生成的交易对数量。
    - num_assets: 资产的种类数量。
    - min_rate: 最小交换比例。
    - max_rate: 最大交换比例。
    - seed: 随机数种子，便于复现结果。

    返回：
    - trading_pairs: 生成的交易对列表，格式为 (asset_a, asset_b, rate)。
    """
    if seed is not None:
        random.seed(seed)

    trading_pairs = []
    assets = [f"Asset_{i}" for i in range(num_assets)]
    existing_pairs = set()

    while len(trading_pairs) < num_pairs:
        a = random.choice(assets)
        b = random.choice(assets)
        if a == b:
            continue
        pair = (a, b)
        if pair in existing_pairs:
            continue
        rate = round(random.uniform(min_rate, max_rate), 6)
        trading_pairs.append([a, b, rate])  # 使用列表而不是元组
        existing_pairs.add(pair)
    return trading_pairs

def update(trading_pairs, num_updates=1, min_rate=0.5, max_rate=1.5):
    """
    随机更新交易对中的交换比例。

    参数：
    - trading_pairs: 交易对列表。
    - num_updates: 要更新的交易对数量。
    - min_rate: 最小交换比例。
    - max_rate: 最大交换比例。

    返回：
    - updated_pairs_indices: 被更新的交易对在列表中的索引。
    """
    updated_pairs_indices = random.sample(range(len(trading_pairs)), num_updates)
    for idx in updated_pairs_indices:
        old_rate = trading_pairs[idx][2]
        new_rate = round(random.uniform(min_rate, max_rate), 6)
        trading_pairs[idx][2] = new_rate
        print(f"交易对 {trading_pairs[idx][0]} -> {trading_pairs[idx][1]} 的交换比例从 {old_rate} 更新为 {new_rate}")
    return updated_pairs_indices