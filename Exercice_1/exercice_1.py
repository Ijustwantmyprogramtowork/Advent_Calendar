import requests
import heapq
import numpy as np
from collections import Counter
import os

def load_data_from_url(
    url="https://adventofcode.com/2024/day/1/input",
    cookies={'session': os.environ.get('AOC_Session')}
):
    """
    Downloads data from a given URL and saves it to a local file.
    This function is deprecated and was intended for one-time use.

    Parameters
    ----------
    url : str, optional
        The URL to fetch the data from. Default is the AoC 2024 Day 1 input.
    cookies : dict, optional
        Authentication cookies required for access. Default is a sample session cookie.
    
    Returns
    -------
    None
    """
    response = requests.get(url, cookies=cookies)
    data = response.text.strip().splitlines()
    
    # Save the downloaded data to a local file
    with open("input_ex_1.txt", "w") as f:
        f.write(response.text.strip())


def load_data(input_file="input_ex_1.txt"):
    """
    Loads and parses data from a local text file into two separate lists of integers.

    Parameters
    ----------
    input_file : str, optional
        Path to the text file containing space-separated integer pairs. Default is "input_ex_1.txt".

    Returns
    -------
    tuple of lists
        A tuple (data_1, data_2) containing the two lists of integers from the left and right columns respectively.
    """
    with open(input_file, "r") as f:
        data = f.read().strip().splitlines()
        
        # Unpack and convert each line into two integer values
        data_1, data_2 = zip(*[(int(a), int(b)) for line in data for a, b in [line.split()]])
        data_1, data_2 = list(data_1), list(data_2)

    return data_1, data_2


def calculate_distance(data_1, data_2):
    """
    Calculates the sum of absolute differences between the corresponding minimum values of two lists.

    The function uses heaps to efficiently extract the minimum values from both lists until they are empty.

    Parameters
    ----------
    data_1 : list of int
        First list of integer values (e.g., left column).
    data_2 : list of int
        Second list of integer values (e.g., right column).

    Returns
    -------
    int
        The total sum of absolute differences between paired minimum elements from the two lists.
    """
    heapq.heapify(data_1)
    heapq.heapify(data_2)
    
    distance = 0

    # Extract and compare minimum elements from each list until both are empty
    while data_1 and data_2:
        min1 = heapq.heappop(data_1)
        min2 = heapq.heappop(data_2)
        distance += np.abs(min1 - min2)

    return distance


def calculate_similarity(data_1, data_2):
    """
    Computes a similarity score between two lists based on frequency of shared values.

    For each value in `data_1`, it is multiplied by the number of times it appears in `data_2`.
    The total sum of these products is returned.

    Parameters
    ----------
    data_1 : list of int
        First list of integer values.
    data_2 : list of int
        Second list of integer values.

    Returns
    -------
    int
        A score representing the similarity based on shared values and frequency.
    """
    counter_2 = Counter(data_2)

    # Sum over (value * frequency in other list)
    score = sum(val * counter_2[val] for val in data_1)
    return score


def main():
    """
    Loads data, computes the distance and similarity between two integer lists,
    and prints the results in a formatted report.
    """
    data_1, data_2 = load_data()
    
    # Compute similarity and distance scores
    score = calculate_similarity(data_1, data_2)
    distance = calculate_distance(data_1, data_2)

    print(f"""
            __________________________________________
            RESULT EXERCISE 1: THE FINAL DISTANCE BETWEEN THE TWO LISTS IS: {distance}

            __________________________________________
            RESULT EXERCISE 2: THE SIMILARITY BETWEEN THE TWO LISTS IS: {score}
    """)


if __name__ == "__main__":
    results = main()
