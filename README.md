# LeetCode Practice

Solutions to LeetCode problems in Python.

## Adding a new problem

```bash
python add.py <problem_number>
```

This will:
- Fetch the problem title, difficulty, and link from LeetCode
- Generate a file in `python/` with the solution stub and example test cases pre-filled
- Print an error if the problem already exists or requires a Premium subscription

**Example:**
```bash
python add.py 53
# Created: python/0053_maximum_subarray.py  [Medium]
```

Once the file is created, fill in your solution. The expected outputs in each `assert` are already filled in.
