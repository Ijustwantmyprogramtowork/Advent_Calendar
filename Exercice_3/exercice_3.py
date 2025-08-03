import re

def extract_instructions(data):
    """
    Extracts all occurrences of the keywords `do()`, `don't()`, and `mul(a, b)` 
    from a string using regular expressions.

    Parameters
    ----------
    data : str
        The raw input text from which to extract instructions.

    Returns
    -------
    list[re.Match]
        A list of match objects containing the matched instructions.
    """
    # Matches either do(), don't(), or mul(X, Y) where X and Y are 1–3 digit numbers
    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")
    return list(pattern.finditer(data))


def compute_enabled_total(instructions):
    """
    Computes the total sum of products from `mul(a, b)` instructions,
    respecting enabling/disabling logic from `do()` and `don't()`.

    Parameters
    ----------
    instructions : list[re.Match]
        A list of regex match objects containing do, don't, and mul instructions.

    Returns
    -------
    int
        The total sum of all enabled `mul(a, b)` products.
    """
    enabled = True
    total = 0

    for match in instructions:
        text = match.group()

        # Toggle enable/disable state
        if text == "do()":
            enabled = True
        elif text == "don't()":
            enabled = False

        # If current instruction is mul(a, b) and enabled, compute the product
        elif enabled:
            a, b = int(match.group(1)), int(match.group(2))
            # Extra safety check on bounds
            if 0 <= a < 1000 and 0 <= b < 1000:
                total += a * b

    return total


def compute_unfiltered_total(data):
    """
    Computes the total sum of all `mul(a, b)` instructions found in the text,
    ignoring any enabling/disabling logic.

    Parameters
    ----------
    data : str
        The input text containing multiple `mul(a, b)` instructions.

    Returns
    -------
    int
        The total sum of all `a * b` for each `mul(a, b)` found.
    """
    # Extract all pairs (a, b) from mul(a, b) calls
    all_muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)

    return sum(int(a) * int(b) for a, b in all_muls)


def main():
    """
    Main execution function.

    Loads instruction data from a local file, extracts all `mul(a, b)` expressions,
    and computes two totals:
    - The unfiltered total: sum of all `a * b` regardless of logic.
    - The filtered total: sum of `a * b` only when enabled via `do()` / `don't()` toggles.

    Outputs both totals to the console.
    """
    # Load the raw text data from file
    with open("input_day_3.txt", "r") as f:
        data = f.read()

    # Part 1: Sum of all mul(a, b) without any filtering
    total = compute_unfiltered_total(data)

    # Part 2: Sum of mul(a, b) only while "enabled"
    instructions = extract_instructions(data)
    filtered_total = compute_enabled_total(instructions)

    print(f"""
    ______________________________________
    TOTAL OF ALL VALID MUL INSTRUCTIONS : {total}
    _____________________________________________
    TOTAL WITH DO()/DON'T() LOGIC APPLIED : {filtered_total}
    """)


if __name__ == "__main__":
    main()
