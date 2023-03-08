# Word Solitaire

Now, for the word list obtained in the previous step, perform word chain following the steps below:

- First, sort the string list;
- Starting with the first word as the head, find a word that starts with the last letter of the current word and add it to the word chain from the remaining words. If it does not exist, save current chain;
- Repeat the previous step in the remaining words until all words have been used up.
  Example:

```python
a = ['a', 'toy', 'has', 'excellent', 'apple']
output:
['a', 'apple', 'excellent', 'toy']
['has']
```

## TODO

- Completing `solitaire.py`

## Requirements
- Each word can only be used once.
- If there are no words, return an empty list.
