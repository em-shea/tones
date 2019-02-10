from numerical_pinyin_converter import convert_from_numerical_pinyin

test_word_list = [
    'huang1 miu4',
    'jian3 shao3',
    'jin3 kuai4',
    'hao4 fei4',
    'ban4 tu2 er2 fei4', 
    'ban4 yan3', 
    'bang1 zhu4',
    'bang3 jia4',
    'nv3 er2',
    'hu2 shuo1',
    'lve4 duo2'
    ]

for word in test_word_list:
    print(convert_from_numerical_pinyin(word))
