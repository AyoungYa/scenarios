import re

def process_sentence(sentence):
    # 去除标点符号、数字及包含字母以外的单词，将所有字母转为小写，并分割为单词列表
    words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    # 去除重复项，相同的单词仅保留一个
    words = list(set(words))
    return words

# 读取用户输入的英语句子
sentence = input("Please enter an English sentence: ")
# 处理并输出单词列表
words = process_sentence(sentence)
print(words)