test_word_list = [
    #'ban4 tu2 er2 fei4', 
    #'ban4 yan3', 
    #'bang1 mang2',
    #'bang1 zhu4',
    #'bang3 jia4',
    'nv3 er2',
    #'bang3 yang4'
    ]

"""pinyin = {
    'a1': 'ā',
    'a2': 'á',
    'a3': 'ǎ',
    'a4': 'à',
    'a5': 'a'
}
"""

"""pinyin = {
    'a': ('ā', 'á', 'ǎ', 'à', 'a'), 
    'e': ('ē', 'é', 'ě', 'è', 'e'),
    'i': ('ī', 'í', 'ǐ', 'ì', 'i'), 
    'o': ('ō', 'ó', 'ǒ', 'ò', 'o'), 
    'u': ('ū', 'ú', 'ǔ', 'ù', 'u'), 
    'v': ('ǖ', 'ǘ', 'ǚ', 'ǜ', 'ü')
}
"""

pinyin = ['ā', 'á', 'ǎ', 'à', 'a']
#e = ['']
#i = []

def find_vowel(letter_list, tonal_pinyin):

    #Identify vowels
    counter = 0
    vowels = []

    print("")
    print("------")
    print("Starting loop for word", letter_list)

    for index, char in enumerate(letter_list):
        if char in 'v':
            char = 'ü'

    for index, char in enumerate(letter_list):
        if char in 'aeiouü':
            counter = counter + 1
            vowels.append(char)
    print("Found vowels", vowels)
    
    print("Checking for multiple vowels")
    if counter > 1:
        if vowels == ['i', 'a']:
            tone_vowel = 'a'
            print("Found multiple vowels", vowels, "Selected", tone_vowel)
        #if vowels == []
    else:
        tone_vowel = ''.join(vowels)
        print("Only one vowel found", tone_vowel)

    #Replace vowel with tonal_pinyin vowel
    letter_list = [w.replace(tone_vowel, tonal_pinyin) for w in letter_list]
    print("Replaced original tone vowel with tonal vowel, new word:", letter_list)

    #Remove extraneous tone number
    tone_number_removed = letter_list[:-1]
    print("Removed now unnecessary tone number:", tone_number_removed)

    #Reform string
    finished_char = "".join(tone_number_removed)
    print("Made the list of letters back into a string:", finished_char)
    return finished_char

def find_tone(word_list):
    
    for word in word_list:
        
        finished_word = []
        # Split into individual character pinyin
        split_word = word.split(' ')
        for indiv_character in split_word:
            
            # Extract tone number from pinyin string
            tone = indiv_character[-1]
            tone_int = int(tone)-1

            #Select matching tonal pinyin vowel from list
            tonal_pinyin = pinyin[tone_int]
            
            # Slice character pinyin into a list
            letter_list = list(indiv_character)
            #print(tonal_pinyin)

            finished_char = find_vowel(letter_list, tonal_pinyin)
            finished_word.append(finished_char)
        print(finished_word)

find_tone(test_word_list)



