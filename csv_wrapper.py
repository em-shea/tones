from numerical_pinyin_converter import convert_from_numerical_pinyin
import csv

with open('hsk_level_6.csv') as fh:
  reader = csv.DictReader(fh)
  for row in reader:
    numerical_pinyin_word = row['Pronunciation']
    new_word = convert_from_numerical_pinyin(numerical_pinyin_word)
    print(new_word)