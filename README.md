# Stock Market Analysis Toolkit

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive toolkit for analyzing stock market data and calculating financial metrics.

## Features
- Historical data download
- Beta coefficient calculation
- Automated CSV exports
- Visualization tools

## Quick Start
```bash
git clone https://github.com/yourusername/stock-market-analysis.git
cd stock-market-analysis
pip install -r requirements.txt

# Run analysis
python src/main.py -t AAPL GOOG -s 2020-01-01 -e 2024-01-01

# Export data
python scripts/publish_data.py -t MSFT -s 2020-01-01 -e 2024-01-01 -o msft_data.csv
