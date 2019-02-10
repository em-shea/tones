from numerical_pinyin_converter import convert_from_numerical_pinyin

test_word_list = [
    'ban4 tu2 er2 fei4', 
    'ban4 yan3', 
    'bang1 mang2',
    'bang1 zhu4',
    'bang3 jia4',
    'nv3 er2',
    'bang3 yang4'
    ]

for word in test_word_list:
    print(convert_from_numerical_pinyin(word))
