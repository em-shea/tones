test_word_list = [
    #'ban4 tu2 er2 fei4', 
    #'ban4 yan3', 
    #'bang1 mang2',
    #'bang1 zhu4',
    'bang3 jia4',
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
        if char in 'aeiou':
            counter = counter + 1
            vowels.append(char)
    print("Found vowels", vowels)
    
    if counter > 1:
        print(vowels)



    #Replace vowel with tonal_pinyin vowel
    letter_list = [w.replace(char, tonal_pinyin) for w in letter_list]

    #Remove extraneous tone number
    tone_number_removed = letter_list[:-1]

    #Reform string
    finished_char = "".join(tone_number_removed)
    return finished_char
    #print(finished_char)

def find_tone(word_list):
    for word in word_list:
        
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


find_tone(test_word_list)



