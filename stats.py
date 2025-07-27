def count_words(text):
    word_count = text.split()
    return len(word_count)

def character_counter(text):
    dictionary={}
    for char in text.lower():
        if not char.isalpha():
            pass
        elif char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char]+=1
    return dictionary

def sort_on(items):
    return items["num"]

def list_of_dictionaries(dictionary):
    list = []
    for pair in dictionary:
        list.append({"char": pair, "num": dictionary[pair]})
    list.sort(reverse=True, key=sort_on)
    return list

