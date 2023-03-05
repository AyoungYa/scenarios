# Word Solitaire

Now, for the word list obtained in the previous step, perform word chain following the steps below:

- First, sort the string list;
- Starting with the first word as the head, find the letters that end the current word from the remaining words. If it does not exist, print the words that have already been chained;
- Repeat the previous step in the remaining words until all words have been used up.
  Example:

```python
a = ['a', 'toy', 'has', 'excellent', 'apple']
output:
['a', 'apple', 'excellent', 'toy']
['has']
```

## TODO

- Completing `word.py`

## Requirements

-
-
