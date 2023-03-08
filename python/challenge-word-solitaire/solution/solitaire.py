def sub_chain(result, words):
    # 用来存储已经接龙的单词
    chains = []
    # 从第一个单词开始
    current_word = words[0]
    # 从剩余的单词中进行查找
    for word in words[1:]:
        # 如果找到了以当前单词结尾的单词，将其加入接龙列表，作为新的当前单词
        if word.startswith(current_word[-1]):
            chains.append(current_word)
            current_word = word
    # 将最后一个单词加入接龙列表
    chains.append(current_word)
    # 去除接龙列表中重复的单词
    chains = list(set(chains))
    # 去除单词列表中已经被使用的单词
    remaining_words = [word for word in words if word not in chains]
    # 如果还有剩余的单词，递归进行单词接龙，直到所有单词都被使用完
    if remaining_words:
        result.append(chains)
        sub_chain(result, remaining_words)
    else:
        result.append(chains)

def word_chain(words):
    result = []
    # 对单词列表进行排序
    words.sort()
    sub_chain(result, words)

    return result


# 输入单词列表
words = ['a', 'toy', 'has', 'excellent', 'apple']
# 进行单词接龙
word_chain(words)
