DEBUG_ENABLED = True

test_word = 'lve4 duo2' #'hu2 shuo1' # 'hao4 fei4' #'bang3 jia4' #'nv3 er2' #jin3 kuai4 jian3 shao3 huang1 miu4 

pinyin = {
    'a': ['ā', 'á', 'ǎ', 'à', 'a'], 
    'e': ['ē', 'é', 'ě', 'è', 'e'],
    'i': ['ī', 'í', 'ǐ', 'ì', 'i'], 
    'o': ['ō', 'ó', 'ǒ', 'ò', 'o'], 
    'u': ['ū', 'ú', 'ǔ', 'ù', 'u'], 
    'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ', 'ü']
}

def debug(*args, **kwargs):
    if DEBUG_ENABLED:
        print(*args, **kwargs)

def convert_to_numerical_pinyin(word):

    finished_word = []
    split_word = word.split(' ')
    for indiv_character in split_word:
        finished_char = convert_indiv_character(indiv_character)
        finished_word.append(finished_char)

    return " ".join(finished_word)

def convert_indiv_character(indiv_character):

    debug("")
    debug("------")
    debug("Starting loop for word:", indiv_character)

    # Convert indiv char string into list of letters
    letter_list = list(indiv_character)

    # Select tone as last item in letter_list
    # Set integer to look up tone in list by  
    tone = letter_list[-1]
    tone_int = int(tone)-1

    debug("Found tone", tone)

    for index, char in enumerate(letter_list):
        if char in 'v':
            letter_list[index] = 'ü'
    debug(letter_list)

    counter = 0
    vowels = []
    
    for index, char in enumerate(letter_list):
        if char in 'aeiouü':
            counter = counter + 1
            vowels.append(char)
    debug("Found vowels:", vowels)

    debug("Checking for multiple vowels")
    
    if counter > 1:
        debug("Found multiple vowels, count:", counter)

        if 'a' in vowels:
            tone_vowel = 'a'
        elif 'o' in vowels:
            tone_vowel = 'o'
        elif 'e' in vowels:
            tone_vowel = 'e'
        else: 
            tone_vowel = vowels[1]

        debug("Selected vowel:", tone_vowel)    
    else:
        tone_vowel = vowels[0]
        debug("Only one vowel found:", tone_vowel)

    tonal_pinyin = pinyin[tone_vowel][tone_int]
    debug(tonal_pinyin)

    return replace_tone_vowel(letter_list, tone_vowel, tonal_pinyin)
    
def replace_tone_vowel(letter_list, tone_vowel, tonal_pinyin):
    
    letter_list = [w.replace(tone_vowel, tonal_pinyin) for w in letter_list]
    debug("Replaced original tone vowel with tonal vowel, new word:", letter_list)

    #Remove extraneous tone number
    tone_number_removed = letter_list[:-1]
    debug("Removed now unnecessary tone number:", tone_number_removed)

    #Reform string
    finished_char = "".join(tone_number_removed)
    debug("Made the list of letters back into a string:", finished_char)
    return finished_char

converted_word = convert_to_numerical_pinyin(test_word)
print(converted_word)