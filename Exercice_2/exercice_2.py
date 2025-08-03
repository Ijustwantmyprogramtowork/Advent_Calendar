import numpy as np
import requests

def is_safe(report):
    """
    Determines whether a report (a list of integers) is considered "safe".

    A report is safe if:
    - It is strictly increasing or strictly decreasing, AND
    - The difference between any two consecutive values is between 1 and 3 (inclusive).

    Parameters
    ----------
    report : list of int
        A list of integer values representing a report.

    Returns
    -------
    bool
        True if the report meets the safety criteria, False otherwise.
    """
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]

    # Check if the report is strictly increasing or strictly decreasing
    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
        # Check if each difference is between 1 and 3
        return all(1 <= abs(d) <= 3 for d in diffs)

    return False


def is_safe_reports(data):
    """
    Splits raw data into individual reports and classifies them as safe or unsafe.

    Parameters
    ----------
    data : list of str
        Each element is a string representing a space-separated list of integers (a report).

    Returns
    -------
    tuple of list of list of int
        A tuple (safe_reports, unsafe_reports), where each report is a list of integers.
    """
    # Convert string data into a list of integer lists (reports)
    reports = [[int(x) for x in line.split()] for line in data]

    # Separate the reports based on whether they are safe
    safe_reports = [r for r in reports if is_safe(r)]
    unsafe_reports = [r for r in reports if not is_safe(r)]

    return safe_reports, unsafe_reports


def is_safe_possible(report):
    """
    Determines whether an unsafe report can be made safe by removing a single element.

    This checks two cases:
    1. The report is almost strictly increasing or decreasing, with one anomaly that,
       if removed (either the anomaly or its neighbor), makes it safe.
    2. The report has a single jump greater than 3, which can be corrected by removing
       one of the two values that cause the jump.

    Parameters
    ----------
    report : list of int
        A report that is not initially considered safe.

    Returns
    -------
    bool
        True if the report can be made safe by removing one element, False otherwise.
    """
    diffs = np.diff(report)
    signs = np.sign(diffs)

    # Case 1: One sign inconsistency in otherwise strictly increasing or decreasing sequence
    if (np.sum(signs > 0) == len(signs) - 1 and np.sum(signs <= 0) == 1):
        idx = np.where(signs <= 0)[0][0]
        for remove_index in [idx, idx + 1]:
            fixed = report[:remove_index] + report[remove_index + 1:]
            if is_safe(fixed):
                return True

    if (np.sum(signs < 0) == len(signs) - 1 and np.sum(signs >= 0) == 1):
        idx = np.where(signs >= 0)[0][0]
        for remove_index in [idx, idx + 1]:
            fixed = report[:remove_index] + report[remove_index + 1:]
            if is_safe(fixed):
                return True

    # Case 2: One large jump (greater than 3) can be resolved by removing one value
    jumps = np.abs(diffs)
    if np.sum(jumps > 3) == 1:
        idx = np.where(jumps > 3)[0][0]
        for remove_index in [idx, idx + 1]:
            fixed = report[:remove_index] + report[remove_index + 1:]
            if is_safe(fixed):
                return True

    return False


def main():
    """
    Loads report data from a local file, identifies safe and unsafe reports,
    and determines which unsafe reports can be corrected by removing one value.
    Prints statistics about safe reports.
    """
    with open("input_day_2.txt", "r") as f:
        data = f.read().strip().splitlines()

    # Classify reports
    safe_reports, unsafe_reports = is_safe_reports(data)

    # Check if unsafe reports can be corrected
    finally_safe = [r for r in unsafe_reports if is_safe_possible(r)]

    # Print results
    print(f"""
        ________________________________
        Number of safe reports: {len(safe_reports)}
        ________________________________________________
        Number of safe reports with new rules: {len(safe_reports) + len(finally_safe)}
    """)
    return


if __name__ == "__main__":
    main()
