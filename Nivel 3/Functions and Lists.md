# Functions and Lists - Word Analyzer

##  Description

This project analyzes a list of words using functions, loops, lists, dictionaries, and string operations.

The program demonstrates:

- Functions
- Lists
- Loops (`for`)
- Dictionaries
- String manipulation
- List comprehensions
- Boolean values
- Basic text analysis

##  Objectives

The program can:

- Display all words in the list.
- Count the total number of words.
- Find the longest word.
- Count how many times a specific word appears.
- Build a frequency dictionary.
- Filter words by minimum length.
- Detect palindromes.
- List all palindromes found.

##  Source Code

```python
def show_word(words):
    print("Words:", " ".join(words))
    print(f"Total: {len(words)}")


def longest_word(words):
    if not words:
        return None

    longest = words[0]

    for w in words:
        if len(w) > len(longest):
            longest = w

    return longest


def count_word(words, target):
    target = target.lower()
    count = 0

    for w in words:
        if w.lower() == target:
            count += 1

    return count


def word_frecuencies(words):
    freq = {}

    for w in words:
        key = w.lower()
        freq[key] = freq.get(key, 0) + 1

    return freq


def filter_by_length(words, min_len):
    return [w for w in words if len(w) >= min_len]


def is_palindrome(word):
    w = word.lower()
    return w == w[::-1]


def palindromes_in(words):
    return [w for w in words if is_palindrome(w)]


def main():
    words = [
        "python", "code", "loop", "function", "list",
        "string", "if", "else", "for", "while",
        "variable", "python", "code", "list",
        "python", "radar", "level"
    ]

    show_word(words)
    print(f"Longest word: {longest_word(words)}")
    print(f"'python' appears: {count_word(words, 'python')} times")
    print(f"Frequencies: {word_frecuencies(words)}")
    print(f"Words with length >= 6: {filter_by_length(words, 6)}")
    print(f"Palindromes: {palindromes_in(words)}")


if __name__ == "__main__":
    main()
```

##  Function Breakdown

### `show_word(words)`

Displays all words separated by spaces and prints the total number of words.

Example:

```python
show_word(words)
```

Output:

```text
Words: python code loop ...
Total: 17
```

### `longest_word(words)`

Returns the longest word in the list.

If the list is empty, returns `None`.

Example:

```python
longest_word(words)
```

Output:

```text
'function'
```

### `count_word(words, target)`

Counts how many times a word appears in the list.

The comparison is case-insensitive using `lower()`.

Example:

```python
count_word(words, "python")
```

Output:

```text
3
```

### `word_frecuencies(words)`

Builds a dictionary containing the frequency of each word.

Example:

```python
{
    'python': 3,
    'code': 2,
    'list': 2
}
```

Key line:

```python
freq[key] = freq.get(key, 0) + 1
```

Meaning:

- If the word already exists, increase its count.
- If it does not exist, start at 0 and add 1.

### `filter_by_length(words, min_len)`

Returns a new list containing only words whose length is greater than or equal to `min_len`.

Example:

```python
filter_by_length(words, 6)
```

Output:

```text
['python', 'function', 'string', 'variable']
```

Uses a list comprehension:

```python
[w for w in words if len(w) >= min_len]
```

### `is_palindrome(word)`

Checks whether a word reads the same forwards and backwards.

Examples:

```python
is_palindrome("radar")
```

Output:

```text
True
```

```python
is_palindrome("python")
```

Output:

```text
False
```

The expression `w[::-1]` creates a reversed copy of the string.

### `palindromes_in(words)`

Returns all palindrome words found in the list.

Example:

```python
['radar', 'level']
```

This function reuses `is_palindrome()` instead of duplicating logic.

##  Concepts Learned

During this exercise I practiced:

- Function creation
- Function calls
- Returning values with `return`
- Working with lists
- List indexing
- String methods
  - `lower()`
  - `len()`
- Dictionaries
  - `.get()`
- Boolean values (`True` / `False`)
- List comprehensions
- String slicing (`[::-1]`)
- Input validation with `if not words:`
- Program entry point: `if __name__ == "__main__":`

##  Sample Output

```text
Words: python code loop function list string if else for while variable python code list python radar level
Total: 17
Longest word: function
'python' appears: 3 times
Frequencies: {'python': 3, 'code': 2, 'loop': 1, 'function': 1, 'list': 2, 'string': 1, 'if': 1, 'else': 1, 'for': 1, 'while': 1, 'variable': 1, 'radar': 1, 'level': 1}
Words with length >= 6: ['python', 'function', 'string', 'variable', 'python', 'python']
Palindromes: ['radar', 'level']
```

---

This project was completed as part of my Python learning journey, focusing on functions, lists, dictionaries, and string manipulation fundamentals.
