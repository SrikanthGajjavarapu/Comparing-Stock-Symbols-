# Stock Portfolio Analysis

## Overview

This project involves creating a stock portfolio using a specific active stock selection strategy and comparing its performance with a benchmark (Nifty50 index). The main objectives include creating classes for handling stock data, implementing the active stock selection strategy, summarizing performance metrics, and visualizing equity curves.

## Project Structure

The project is organized into the following components:

- **stock.py**: Contains the `Stock` class for handling individual stock data.
- **benchmark.py**: Implements the `Benchmark` class for downloading and managing benchmark data (Nifty50 index).
- **portfolio.py**: Defines the `Portfolio` class, which handles the active stock selection strategy, performance metrics, and data visualization.
- **main.py**: A script demonstrating the usage of the classes and generating analysis results.

## Usage

To run the project, follow these steps:

Run the main script:

    ```bash
    python main.py
    ```

## Dependencies

- **yfinance**: Used for downloading historical stock data.
- **pandas**: Used for handling and manipulating data.
- **numpy**: Required for numerical operations.
- **matplotlib**: Used for data visualization.
- **streamlit**: Used for creating the app for presenting performance metrics.

## Configuration

Adjust the symbols, start date, and end date in the `main.py` script according to your requirements.

## App

The project includes an app built with Streamlit for presenting performance metrics. To run the app:

```bash
streamlit run app.py
