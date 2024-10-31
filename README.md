# Arbitrage Detection Demo Program

This program simulates real-time arbitrage detection in a trading network with multiple assets and trading pairs. It uses graph algorithms to find the most profitable trading cycles (arbitrage opportunities) and updates in real-time as trading pairs’ exchange rates change.

## Features

- **Real-time Arbitrage Detection**: Continuously monitors trading pairs and detects the most profitable trading cycles.
- **Interactive Command-Line Interface**: Allows users to start, stop, and exit the program using simple commands.
- **Dynamic Updates**: Simulates real-time updates of exchange rates and recalculates the most profitable cycles accordingly.
- **Performance Metrics**: Displays runtime statistics, including program start time, duration, and the number of times the optimal path has changed.

## Installation

### Prerequisites

- Python 3.6 or higher

Clone the Repository

```bash
https://github.com/Ysrae1/Arb-Detection-Demo.git
cd Arb-Detection-Demo
```

### Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Directory Structure

.
├── main.py
├── requirements.txt
└── lib
    ├── __init__.py
    ├── ArbDataStruct.py
    └── TradingPairs.py

- `main.py`: The main script to run the program.
- `requirements.txt`: Contains the list of required Python packages.
- `lib/`: Directory containing the supporting modules.
  - `ArbDataStruct.py`: Contains functions related to arbitrage data structures and algorithms.
  - `TradingPairs.py`: Contains functions for generating and updating trading pairs.

## Usage

Run the main script using Python:

```bash
python main.py
```

### Command-Line Interface

- **Start/Stop the Program**: Press `'s'` to start or stop the arbitrage detection.
- **Exit the Program**: Press `'e'` to exit the program.

### Example Interaction

```bash
输入 's' 开始，'e' 退出：s
开始更新和检测套利机会。

套利检测程序正在运行...
开始时间：2023-10-31 12:00:00
持续时间：00:00:05
最优路径变动次数：3

模拟实时更新交易对：
交易对 Asset_31 -> Asset_28 的交换比例从 1.046166 更新为 0.949307
交易对 Asset_0 -> Asset_36 的交换比例从 1.406055 更新为 1.495834
...
更新受影响的回路...
更新受影响的回路耗时：0.012960 秒
最盈利的回路：(('Asset_2', 'Asset_20'), ('Asset_20', 'Asset_25'), ('Asset_25', 'Asset_23'), ('Asset_23', 'Asset_2'))，盈利：2.712626
获取最盈利的回路耗时：0.000009 秒
```

### Program Output

- **Program Start Time**: The time when the program started running.
- **Duration**: The elapsed time since the program started.
- **Optimal Path Change Count**: The number of times the most profitable cycle has changed.
- **Exchange Rate Updates**: Shows which trading pairs have been updated and their new exchange rates.
- **Performance Metrics**: Displays the time taken to update affected cycles and retrieve the most profitable cycle.

## Configuration

You can adjust the following parameters in `main.py`:

- **Number of Trading Pairs**: Adjust `num_pairs` in `tp.generator()` to increase or decrease the number of trading pairs.
- **Number of Assets**: Adjust `num_assets` in `tp.generator()` to change the number of assets in the simulation.
- **Maximum Cycle Length**: Adjust `max_length` in `arb.find_cycles()` to control the maximum length of cycles considered.
- **Update Interval**: Adjust `update_interval` to change the time interval between updates.
Requirements

## Requirements

All required packages are part of the Python Standard Library. However, ensure you have the following:

- `Python 3.6` or higher
- Standard libraries:
  - `threading`
  - `time`
  - `os`
  - `sys`

**Note**: If `lib` modules (`ArbDataStruct.py` and `TradingPairs.py`) use any external packages, include them in the `requirements.txt` file.

## Notes

- The program uses ANSI escape codes to control terminal output. Ensure your terminal emulator supports ANSI codes.
- The program is designed for educational purposes to simulate arbitrage detection and may not be suitable for real-world financial applications without further development and testing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
