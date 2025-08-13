def get_num_words(text):
    list=text.split()
    num_of_words=len(list)
    return num_of_words

def get_char_count(text):
    char_count={}
    for char in text.lower():
        if char in char_count.keys():
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count

def format_count(dict):
    list=[]
    for char in dict:
        temp={"char": char, "num": dict[char]}
        list.append(temp)
    list.sort(key=lambda item: item['num'], reverse=True)
    return list
