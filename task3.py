#!/usr/bin/env python3

import argparse
import re
from typing import Iterable, Dict, List
from collections import Counter
from tabulate import tabulate


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parses a single log line into a dictionary.

    Args:
        line (str): A line from the log file.

    Returns:
        dict: A dictionary containing 'date', 'time', 'level', and 'text' if the line matches the expected format,
              otherwise None.
    """
    match = re.match(
        r"(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<level>[A-Z]+)\s+(?P<text>.+)",
        line,
    )
    if match:
        return {
            "date": match.group("date"),
            "time": match.group("time"),
            "level": match.group("level"),
            "text": match.group("text"),
        }


def load_logs(path: str) -> Iterable[Dict[str, str]]:
    """
    Loads logs from a file and yields parsed log lines.

    Args:
        path (str): The path to the log file.

    Yields:
        dict: Parsed log lines as dictionaries.
    """
    with open(path, "r", encoding="UTF-8") as file:
        for line in file:
            yield parse_log_line(line)


def filter_log_by_level(
    logs: List[Dict[str, str]], level: str
) -> Iterable[Dict[str, str]]:
    """
    Filters logs by the specified log level.

    Args:
        logs (list): A list of log dictionaries.
        level (str): The log level to filter by.

    Returns:
        Iterable[dict]: Filtered logs that match the specified log level.
    """
    return filter(
        lambda log: log["level"].strip().lower() == level.strip().lower(), logs
    )


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Counts occurrences of each log level in the logs.

    Args:
        logs (list): A list of log dictionaries.

    Returns:
        dict: A dictionary with log levels as keys and their counts as values.
    """
    levels = map(lambda log: log["level"], logs)
    levels_counter = Counter(levels)
    return dict(levels_counter)


def main():
    """
    Main function to execute the log reader script.

    It processes command line arguments to specify the log file path and an optional log level for filtering.
    The statistics of log levels are displayed, along with details for the specified log level if provided.
    """
    parser = argparse.ArgumentParser(description="Читач логів")
    parser.add_argument("path", type=str, help="Обов'язковий параметр: шлях до файлу")
    parser.add_argument(
        "level",
        nargs="?",
        help="Необов'язковий параметр: для відображення записів з певним рівнем логування",
    )

    args = parser.parse_args()

    path = args.path
    level = args.level

    # Load logs from the specified file path
    logs = list(load_logs(path))

    # Count occurrences of each log level
    logs_statistics = count_logs_by_level(logs)
    print(
        tabulate(
            list(logs_statistics.items()),
            headers=["Рівень логування", "Кількість"],
            tablefmt="fancy_grid",
        )
    )

    # If a log level is specified, filter and display those logs
    if level:
        level_logs = filter_log_by_level(logs, level)
        print(f"Деталі логів для рівня '{level}':")
        for log in level_logs:
            print(f'{log["date"]} {log["time"]} - {log["text"]}')


if __name__ == "__main__":
    main()
