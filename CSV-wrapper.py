with open('file.csv') as fh:
  for row in fh:
    new_word = numeric_pinyin_conversion(row)
    print(new_word)