# Advent Calendar

**Challenge ID:** `ownerproof-5068551-1753810021-9eb9e1a97b96`  
**GitHub Username:** `Ijustwantmyprogramtowork`

---

## Day 1

Used requests to download data from an HTTPS URL and saved it locally. This method was reused across all exercises.

Applied heapq to extract the minimum values and computed the absolute distance between them.

To calculate similarity, used collections.Counter to count occurrences of each number in both the left and right lists.

**To execute:**
```bash
cd Exercice_1
python exercice_1.py
```

## Day 2: 

Calculated differences between report values. The first check determined whether the values were strictly increasing or decreasing. The second check verified that all differences were between 1 and 3.

For the second part, analyzed reports marked as "not safe." Checked whether one differing value was the opposite of the others (indicating it could be salvaged). If so, removed that value and rechecked using the initial function. Also handled cases where a jump exceeded 3 by removing the value and reevaluating safety.

**To execute:**
go to root base,
```bash
cd Exercice_2
python exercice_2.py
```

## Day 3

Used regular expressions (re) to identify all occurrences of mul(x, y) where x and y are natural numbers and both less than \(10^3\). If a match was found, the result of the multiplication (x * y) was added to a running total.

In the second part, implemented a dynamic traversal to check whether do or don't instructions appeared before each mul expression. If the instruction was do, the multiplication result was included in the sum. If it was don't, the result was ignored.

**To execute:**
go to root base,
```bash
cd Exercice_3
python exercice_3.py
```


## Day 4

Traversed all the letters in the matrix to check in every direction for occurrences of the word "XMAS". Each time it was found, incremented a counter and returned the total count.

For the second part, started from the letter 'A' (the middle of the word) and checked diagonally for the words "MAS" or "SAM", counting each occurrence.

**To execute:**
go to root base,
```bash
cd Exercice_4
python exercice_4.py
```