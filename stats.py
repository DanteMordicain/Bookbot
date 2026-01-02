def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_num_character(text):
    lowercasetext = text.lower()
    char_count = {}
    for char in lowercasetext:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
    return char_count
     
def sort_on(char_count):
    char_list = []
    for char, num in char_count.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_key)
    return char_list
    
def sort_key(item):
    return item["num"]

    