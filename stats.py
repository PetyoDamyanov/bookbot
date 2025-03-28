def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort_chars(dict):
    sorted_list = []
    for row in dict:
        sorted_list.append({"name": row, "num": dict[row]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list