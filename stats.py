def sort_on(items):
    return items['num']

def get_num_words(content):
    word_list = content.split()
    num_words = len(word_list)
    return num_words

def count_characters(content):
    character_count = {}

    for char in content:
        if char.lower() not in character_count:
           character_count[char.lower()] = 1
        else:
            character_count[char.lower()] += 1
    return character_count

def sort_chars(content):
    char_dict = count_characters(content)
    dict_list = []

    for i in char_dict:
        if i.isalpha():
            a = {'char': i, 'num': char_dict[i]}
            dict_list.append(a)

    dict_list.sort(reverse=True, key=sort_on)

    for i in range(len(dict_list)):
        print(f"{dict_list[i]['char']}: {dict_list[i]['num']}") 

