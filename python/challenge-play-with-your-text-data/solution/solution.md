# Solution

## Step 1 Solution

```python
# count the total number of words in all the files in a directory.
import os

total_len = 0
for f in os.listdir('/home/labex/project/files'):
    total_len += len(open(os.path.join('/home/labex/project/files', f), 'r').read().split())

print(total_len)
```

## Step 2 Solution

```python
# count the top 3 most frequent words in all the files in a directory.
import os

words_counter = {}
for f in os.listdir('/home/labex/project/files'):
    words = open(os.path.join('/home/labex/project/files', f), 'r').read().split()
    for word in words:
        word = word.strip('.,')
        if word not in words_counter:
            words_counter[word] = 0
        words_counter[word] += 1

for words, count in sorted(words_counter.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(words, count)
```

## Step 3 Solution

create output folder:

```bash
mkdir output
```

then, create a python script and execute:

```python
# read multiple files and writes the n-th word of each file to n-th file
import os

words_list = []

max_len = 0

for f in os.listdir('/home/labex/project/files'):
    texts = open(os.path.join('/home/labex/project/files', f), 'r').read().split()
    texts = [text.strip(',.') for text in texts]
    words_list.append(texts)
    max_len = max_len if max_len > len(texts) else len(texts)

for i in range(max_len):
    words = []
    for word_list in words_list:
        if i < len(word_list):
            words.append(word_list[i])
    open(f'/home/labex/project/output/{i+1}', 'w').write(' '.join(words))
```
