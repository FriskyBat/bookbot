def book_num_count(booktext):
    wordlist = booktext.split()
    numwords = len(wordlist)
    return numwords

def book_chara_count(booktext):
    character_counts = {}
    lowertext = booktext.lower()
    
    for chara in lowertext:
        if chara in character_counts:
            character_counts[chara] += 1
        else:
            character_counts[chara] = 1
    return character_counts

def sort_list(items):
        return items["num"]

def sorted_chara_count(character_counts):
    sorted_list = []

    for item in character_counts:
        chara = item
        num = character_counts[item]
        charanumpair = {"chara": chara, "num": num} 

        sorted_list.append(charanumpair)
        
    sorted_list.sort(reverse = True, key = sort_list)
      
    return sorted_list