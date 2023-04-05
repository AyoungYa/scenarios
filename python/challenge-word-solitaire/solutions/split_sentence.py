import re

def process_sentence(sentence):
    result = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    result = list(set(result))
    return result

