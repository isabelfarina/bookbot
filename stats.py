def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
            

    print(f"Found {len(words)} total words")

def count_chars(file_path):
    char_dict = {}
    with open(file_path, 'r') as file:
        text = file.read()
        for words in text:
            for char in words:
                if char.lower() in char_dict:
                    char_dict[char.lower()] += 1
                else:
                    char_dict[char.lower()] = 1
            
    return(char_dict)

def get_num(char_dict):
    return char_dict["num"]

def sort_list(char_dict):
    value = char_dict.values()
    key = list(char_dict.keys())
    new = []
    for key, value in char_dict.items():
        new.append({"char": key, "num": value})
    # sort the dictionary by count from get_num from greatest to least
    new.sort(key=get_num, reverse=True)
    return new