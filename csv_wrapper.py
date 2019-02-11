from numerical_pinyin_converter import convert_from_numerical_pinyin
import csv

with open('hsk_level_6.csv', encoding ="utf8") as fh:
  reader = csv.DictReader(fh)
  new_word_list = []
  for row in reader:
    row['Pronunciation'] = convert_from_numerical_pinyin(row['Pronunciation'])
    new_word_list.append(row)

with open('hsk_level_6_modified.csv', 'w', newline='', encoding ="utf8") as fh:
  fieldnames = list(new_word_list[0].keys())
  writer = csv.DictWriter(fh, fieldnames=fieldnames)
  writer.writeheader()
  
  for row in new_word_list:
    writer.writerow(row)
