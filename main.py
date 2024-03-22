def main():

    print("--- Begin report of books/frankenstein.txt ---")

    with open("books/frankenstein.txt") as f:
        book_string = f.read()

    book_list = book_string.split()
    word_count = len(book_list)
        
    print("\n" + str(word_count) + " words found in the document\n")    

    letter_dict = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
        "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
        "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
        "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0
    }

    for word in book_list:
        for char in word:
            for letter in letter_dict:
                if char.lower() == letter:
                    letter_dict[letter] = letter_dict[letter] + 1
                    break
    
    org_dict = {}

    for letter in letter_dict:
        counter = 0
        for l in letter_dict:
            if letter_dict[letter] > letter_dict[l]:
                counter += 1
        counter = checkRepeats(counter, org_dict)
        org_dict.update({counter: {letter: letter_dict[letter]}})
    
    for i in range(26):
        popped_item = org_dict[25 - i].popitem()
        print("In spot #" + str(i + 1) + "; the letter '" 
              + popped_item[0] + "' appears "
              + str(popped_item[1]) + " times")

    # for letter in dict: count++ if dict[letter] >
    # dict[other letter], then new_dict.append 
    # {count: {letter: dict[letter]}}

def checkRepeats(count, diction):
    for number in diction:
        if count == number:
            return checkRepeats(count + 1, diction)
    return count

main()
